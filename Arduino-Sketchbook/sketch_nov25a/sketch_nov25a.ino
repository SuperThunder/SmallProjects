#include <Arduino.h>

//segments
int a = 8;
int b = 2;
int c = 3;
int d = 4;
int e = 5;
int f = 6;
int g = 7;
//digits
int d1 = 9;
//other
int del = 100;
int buttoncount = 0;
int loopcount = 0;

void setup()
{
  Serial.begin(9600);
  delay(500);//Delay to let system boot
  Serial.println("4 digit 7 segment display test\n\n");
  pinMode(d1, OUTPUT);
  pinMode(a, OUTPUT);
  pinMode(b, OUTPUT);
  pinMode(c, OUTPUT);
  pinMode(d, OUTPUT);
  pinMode(e, OUTPUT);
  pinMode(f, OUTPUT);
  pinMode(g, OUTPUT);
  digitalWrite(d1, LOW);
  digitalWrite(a, LOW);
  digitalWrite(b, LOW);
  digitalWrite(c, LOW);
  digitalWrite(d, LOW);
  digitalWrite(e, LOW);
  digitalWrite(f, LOW);
  digitalWrite(g, LOW);

}

void loop()
{ 
  //Turn display ON
  digitalWrite(d1, HIGH);
  delay(350);
  
  //Turn display OFF
  digitalWrite(d1, LOW);
  delay(650);
  
}

void setlow(){
  digitalWrite(d1, LOW);
  /*
  digitalWrite(a, LOW);
  digitalWrite(b, LOW);
  digitalWrite(c, LOW);
  digitalWrite(d, LOW);
  digitalWrite(e, LOW);
  digitalWrite(f, LOW);
  digitalWrite(g, LOW);
  */
}

void sethigh(){
  digitalWrite(d1, HIGH);
  digitalWrite(a, HIGH);
  digitalWrite(b, HIGH);
  digitalWrite(c, HIGH);
  digitalWrite(d, LOW);
  digitalWrite(e, LOW);
  digitalWrite(f, LOW);
  digitalWrite(g, LOW);
}

