 /* Read Jostick
  * ------------
  *
  * Reads two analog pins that are supposed to be
  * connected to a jostick made of two potentiometers
  *
  * We send three bytes back to the comp: one header and two
  * with data as signed bytes, this will take the form:
  *     Jxy\r\n
  *
  * x and y are integers and sent in ASCII 
  * 
  * http://www.0j0.org | http://arduino.berlios.de
  * copyleft 2005 DojoDave for DojoCorp
  *
  * Taken from https://www.arduino.cc/en/Tutorial/JoyStick
  */

// PS2 joystick (5 pins incl button)
// VRx connected to analog pin 0
// VRy connected to analog pin 1
// SW not connected yet (button pin)

// int ledPin = 13
 int joyPin1 = 0;                 // slider variable connecetd to analog pin 0
 int joyPin2 = 1;                 // slider variable connecetd to analog pin 1
 
 int value1 = 0;                  // variable to read the value from the analog pin 0
 int value2 = 0;                  // variable to read the value from the analog pin 1

 void setup() {
  //pinMode(ledPin, OUTPUT);              // initializes digital pins 0 to 7 as outputs
  Serial.begin(9600);
 }

 int treatValue(int data) {
  return (data * 9 / 1024) + 48;
 }

 void loop() {
  // reads the value of the variable resistor 
  value1 = analogRead(joyPin1);   
  // this small pause is needed between reading
  // analog pins, otherwise we get the same value twice
  delay(100);             
  // reads the value of the variable resistor 
  value2 = analogRead(joyPin2);   

  //digitalWrite(ledPin, HIGH);           
  //delay(value1);
  //digitalWrite(ledPin, LOW);
  //delay(value2);
  
  // X and Y are kind of arbitrary depending on how you orient the joystick
  
  Serial.print("\n\nVal_y: ");
  Serial.print(value1);
  Serial.print("\nVal_x: ");
  Serial.print(value2);
  //Serial.println(treatValue(value2));
  delay(1500);
 }
