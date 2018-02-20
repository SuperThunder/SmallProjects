/* Code from a tutorial on using the OLED screen and another one on using the joystick. Modified to not busyloop using this tutorial:
https://learn.adafruit.com/multi-tasking-the-arduino-part-1/using-millis-for-timing
*/

#include <SPI.h>
#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>

// OLED display TWI address
#define OLED_ADDR   0x3C

Adafruit_SSD1306 display(-1);

#if (SSD1306_LCDHEIGHT != 64)
#error("Height incorrect, please fix Adafruit_SSD1306.h!");
#endif

// JOYSTICK DATA
const int joyPin1 = 0;
const int joyPin2 = 1;
int joyValue1 = 0;
int joyValue2 = 0;
unsigned long lastJoyRead = 0;
const int joyReadWait = 50; // need to wait between the readings of the X and Y potentiometers. This gives us effectively 20FPS on the controls
unsigned long lastJoySerialUpdate = 0;
const int joySerialUpdateInterval = 2000; //send the state of the X and Y knob once a second

//PHYSICS DATA
unsigned long physTimer=0;
const int physInterval=18;

// SCREEN DATA
int centerX = 0;
int centerY = 0;
int circleX = 0;
int circleY = 0;
int previousScreenUpdateMillis = 0;
// For 60 FPS we want about an 18ms wait. Choose whatever lowest FPS is smoothest to reduce power usage.
const int screenUpdateWait = 18;

void setup() {
  // initialize serial for debug values
  Serial.begin(9600);
  
  // initialize and clear display
  display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR);
  display.clearDisplay();
  display.display();

  // display a pixel in each corner of the screen
  display.drawPixel(0, 0, WHITE);
  display.drawPixel(127, 0, WHITE);
  display.drawPixel(0, 63, WHITE);
  display.drawPixel(127, 63, WHITE);

  // Title text
  display.setCursor(8, 0);
  display.setTextColor(WHITE);
  display.setTextSize(1);
  display.print("Joystick+screen demo");
  display.display();
  
  // Center circle - initial
  centerX = display.width()/2;
  circleX = centerX;
  centerY = display.height()/2;
  circleY = centerY;
  display.fillCircle(centerX, centerY, 4, WHITE);
  // Black dot within the circle
  display.fillCircle(display.width()/2, display.height()/2, 2, BLACK); 
  display.display();
}

void loop() {
  // put your main code here, to run repeatedly:
  
  // Timer for state machines to compare with
  unsigned long currentMillis = millis();
  
  //==============================================
  // JOYSTICK CODE
  // To keep things smooth we probably want to check as much or more as the screen updates
  if( currentMillis - lastJoyRead > joyReadWait)
  {  
    joyValue1 = analogRead(joyPin1);           
  }
  // this small pause is needed between reading
  // analog pins, otherwise we get the same value twice
  if( currentMillis - lastJoyRead - 50 > joyReadWait )
  {
     // reads the value of the variable resistor
     joyValue2 = analogRead(joyPin2); 
  }

  if( currentMillis - lastJoySerialUpdate > joySerialUpdateInterval )
  {
    lastJoySerialUpdate = currentMillis;
    // X and Y are kind of arbitrary depending on how you orient the joystick
    Serial.print("\n\nVal_y: ");
    Serial.print(joyValue1);
    Serial.print("\nVal_x: ");
    Serial.print(joyValue2);
    //Serial.println(treatValue(value2));
  }
  //END OF JOYSTICK CODE
  //==============================================
  //START PHYSICS CODE
  //==============================================
  if( currentMillis - physTimer > physInterval) 
  {
    physTimer = currentMillis;
    //Move the circle around
    //Move in X plane
    if( (joyValue1 < 450) && (circleY < 64 ))
    {
      circleY += 1;
    }
    else if( joyValue1 > 550 && (circleY > 0 ) )
    {
      circleY -= 1;
    }
    //Move in Y plane
    if( joyValue2 < 450 && (circleX > 0 ) )
    {
      circleX -= 1;
    }
    else if( joyValue2 > 550 && (circleX < 128 ))
    {
      circleX += 1;
    }
  }
  //END OF PHYSICS CODE
  //==============================================
  //START DISPLAY CODE
  //==============================================
  //Display code - depends on joystick
  if( currentMillis - previousScreenUpdateMillis > screenUpdateWait )
  {
    previousScreenUpdateMillis = currentMillis;
    //Put our base down
    display.clearDisplay();
    // display a pixel in each corner of the screen
    display.drawPixel(0, 0, WHITE);
    display.drawPixel(127, 0, WHITE);
    display.drawPixel(0, 63, WHITE);
    display.drawPixel(127, 63, WHITE);
  
    // Title text
    display.setCursor(4, 0);
    display.setTextColor(WHITE);
    display.setTextSize(1);
    display.print("Joystick+screen demo");
    
    
    // Center circle - can be moved around by joystick
    //display.fillCircle(circleX, circleY, 4, WHITE);
    // Black dot within the circle
    //display.fillCircle(circleX, circleY, 2, BLACK)
    //void drawRect(ui2nt16_t x0, uint16_t y0, uint16_t w, uint16_t h, uint16_t color);
    display.drawRect(32, 16, circleX, circleY, WHITE);
    display.display();
  }
  //END OF DISPLAY CODE
  //============================================
}
