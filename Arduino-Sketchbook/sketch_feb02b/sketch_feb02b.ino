/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led = 13;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);     
}

// the loop routine runs over and over again forever:
void loop() {
  //digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  //delay(1000);               // wait for a second
  //digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  //delay(1000);               // wait for a second
  blink(200, 1000 );
}

//duty cycle % out of 255 and rest/light period in ms
void blink(uint8_t duty, long period)
{
  //we want to wait until the period is over
  //at a 10ms on/off duty cycle this means we want to wait the period divided by that number
  long onloops = period/20;
  //on cycle
  for( long cycles = 0; cycles < onloops; cycles++ )
  {
    digitalWrite(led, HIGH);
    delay(10);
    digitalWrite(led, LOW);
    delay(10);
  }
  
  //off cycle
  digitalWrite(led, LOW);
  delay(period);
}
