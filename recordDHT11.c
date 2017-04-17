#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#define MAXTIMINGS	85 //somehow this corresponds to GPIO 4
#define DHTPIN		7
int dht11_dat[5] = { 0, 0, 0, 0, 0 };
int good, bad;
// Pins:
// Connect - on DHT11 to Ground on Pi
// Connect + on DHT11 to 5V on Pi
// Connect Signal on DHT11 to (in this case) GPIO 4 on Pi

//modified version of a given program from some website
//http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/ 
//^maybe this
//https://projects.drogon.net/raspberry-pi/wiringpi/download-and-install/
//^get wiringpi installed first, then
//gcc -o example example.c -lwiringPi -lwiringPiDev 

// TODO: Fully implement humidity and write a proper read_dht11_dat
// Rewrite this all in C++?
int read_dht11_dat( float* temp, float* humidity )
{
	uint8_t laststate	= HIGH;
	uint8_t counter		= 0;
	uint8_t j		= 0, i;
 
	dht11_dat[0] = dht11_dat[1] = dht11_dat[2] = dht11_dat[3] = dht11_dat[4] = 0;
 
	//a lot of error likely results from here - we need microsecond level delay
	pinMode( DHTPIN, OUTPUT );
	digitalWrite( DHTPIN, LOW );
	delay( 50 ); //changed this from 18, improved things greatly
	// 18ms MINIMUM, see: https://akizukidenshi.com/download/ds/aosong/DHT11.pdf
	digitalWrite( DHTPIN, HIGH );
	delayMicroseconds( 40 ); //this should probably be 40
	pinMode( DHTPIN, INPUT );
 
	for ( i = 0; i < MAXTIMINGS; i++ )
	{
		counter = 0;
		while ( digitalRead( DHTPIN ) == laststate )
		{
			counter++;
			// void delayMicroseconds (unsigned int howLong) -> wraps after 71 minutes
			delayMicroseconds( 1 );
			if ( counter == 255 )
			{
				break;
			}
		}
		laststate = digitalRead( DHTPIN );
 
		if ( counter == 255 )
			break;
 
		if ( (i >= 4) && (i % 2 == 0) )
		{
			dht11_dat[j / 8] <<= 1;
			if ( counter > 16 )
				dht11_dat[j / 8] |= 1;
			j++;
		}
	}
 
	if ( (j >= 40) &&
	     (dht11_dat[4] == ( (dht11_dat[0] + dht11_dat[1] + dht11_dat[2] + dht11_dat[3]) & 0xFF) ) )
	{
		//f = dht11_dat[2] * 9. / 5. + 32;
		//printf( "Humidity = %d.%d %% Temperature = %d.%d C (%.1f F)\n",
			//dht11_dat[0], dht11_dat[1], dht11_dat[2], dht11_dat[3], f );
		++good;
		// Currently only using the integer and not decimal digits, would be accurate except for fact this ignores rounding
		*temp = dht11_dat[2];
		*humidity = dht11_dat[0];
		//TODO: add rest of digits dht11_dat[3]/100.0;
		return 1;
	} else {
		//printf( "Data not good, skip\n" );
		//I think it considers it bad if the checksum (dht11_dat[4]) doesn't match the individual parts
		//if the raspberry pi is under generally heavier load (even a burst load)
	//then the delay introduced by the kernel switching tasks seems to cause bad reasdings
		fprintf(stderr, "BAD: %d.%d C\n", dht11_dat[2], dht11_dat[3]);
		++bad;
		return 0;
	}
}
 
/* What we want to do in terms of long term data collection is get a result every 30s
 * or 60s or so.
 * however, the failure rate is so high we need to make sure we get a
 * valid value
 */

int main( void )
{
	//printf( "Raspberry Pi wiringPi DHT11 Temperature test program\n" );
	good = bad = 0;
	float temp;
	float humidity;
	//char strInputFilename[30];
	//char strOutputFilename[30];
	//FILE* out;

	// To use wiringPi functins you need to call a wiringPi setup function
	if ( wiringPiSetup() == -1 )
		exit( 1 );
	
	//printf("Enter filename (including .csv): ");
	//scanf("%s", strInputFilename);
	//printf("%s\n", strInputFilename);
	//snprintf( strOutputFilename, sizeof(strOutputFilename), "%s", strInputFilename);
	//printf("%s\n", strOutputFilename);
	
	// Repeat the polling function until we get a valid measurement
	// Then wait enough to start on the next minute
	
		//TODO: get a value every n seconds
		int retries = 0;
		//open and close file in loop so that it updates
		//the program may also eventually experience long delays
		//so makes sense to not always have file open
		//out = fopen("templog.csv", "a");
		//out = fopen(strOutputFilename, "a");
		
		while( !(read_dht11_dat(&temp, &humidity)) )
		{
			//wait 1000ms until retry
			delay( 1000 );
			retries++;
			
			//make it retry silently on bad values up to 10
			if(retries > 10){
				fprintf(stderr, "%d Consecutive Read Errors,\n", retries);
			}
		}
		
		//once we have right value, put it in here
		time_t t;
		struct tm * dt;
		time( &t );
		dt = localtime ( &t );
		
		//printf("Got valid: %.2f\n", temp);
		
		//TODO: replace sketchy CSV system with sqlite3
		//ALSO: Find out why the recording intermitently fails
		//put the time in the file, note no newline here
		fprintf(stdout, "%.24s,", asctime(dt) );
		//fprintf("%d-%d-%d %d:%d:%d,", dt.tm_year + 1900, dt.tm_mon + 1, dt.tm_mday, dt.tm_hour, dt.tm_min, dt.tm_sec);
		//put the values in the file
		fprintf(stdout, "%.2f,%.2f,", temp, humidity);
		
		//print the stats on errors and the current time
		//printf("%.24s,", asctime(dt));
		//fprintf(stderr, "Good: %d Bad: %d Perc: %.1f\n", good, bad, (100.0*good)/(bad+good) );
		
	
	
 
	return 0;
}

