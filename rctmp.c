#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#define MAXTIMINGS	85 //somehow this corresponds to GPIO 4
#define DHTPIN		7
int dht11_dat[5] = { 0, 0, 0, 0, 0 };
int good, bad;

//modified version of a given program from some website

int read_dht11_dat(float* temp)
{
	uint8_t laststate	= HIGH;
	uint8_t counter		= 0;
	uint8_t j		= 0, i;
	//float	f; 
 
	dht11_dat[0] = dht11_dat[1] = dht11_dat[2] = dht11_dat[3] = dht11_dat[4] = 0;
 
	//a lot of error likely results from here - we need microsecond level delay
	pinMode( DHTPIN, OUTPUT );
	digitalWrite( DHTPIN, LOW );
	delay( 50 ); //changed this from 18, improved things greatly
	digitalWrite( DHTPIN, HIGH );
	delayMicroseconds( 40 ); //this should probably be 40
	pinMode( DHTPIN, INPUT );
 
	for ( i = 0; i < MAXTIMINGS; i++ )
	{
		counter = 0;
		while ( digitalRead( DHTPIN ) == laststate )
		{
			counter++;
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
		*temp = dht11_dat[2];
		//TODO: add rest of digits dht11_dat[3]/100.0;
		return 1;
	}else  {
		//printf( "Data not good, skip\n" );
		//I think it considers it bad if the checksum (dht11_dat[4]) doesn't match the individual parts
		printf("BAD: %d.%d C\n", dht11_dat[2], dht11_dat[3]);
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
	printf( "Raspberry Pi wiringPi DHT11 Temperature test program\n" );
	good = bad = 0;
	float temp;
	FILE* out;

	if ( wiringPiSetup() == -1 )
		exit( 1 );
	
	while ( good + bad < 100 )
	{	
		//open and close file in loop so that it updates
		//the program may also eventually experience long delays
		//so makes sense to not always have file open
		out = fopen("templog.csv", "a");
		
		//TODO: make it retry on bad value
		//TODO: get a value every n seconds
		if(read_dht11_dat(&temp))
		{
			//TODO: get a time and date inserted here too
			printf("Got valid: %.2f\n", temp);
			fprintf(out, "%.2f C,\n", temp);
		}
		else
		{
			
		}
		printf( "Good: %d Bad: %d Perc: %.1f\n", good, bad, (100.0*good)/(bad+good) );
		
		fclose(out);
		//probably VERY BAD to have less than 1s between readings
		delay( 1000 ); 
	}
	
	
 
	return(0);
}
