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

/*
// JOYSTICK DATA
const int joyPin1 = 0;
const int joyPin2 = 1;
int joyValue1 = 0;
int joyValue2 = 0;
unsigned long lastJoyRead = 0;
const int joyReadWait = 50; // need to wait between the readings of the X and Y potentiometers. This gives us effectively 20FPS on the controls
unsigned long lastJoySerialUpdate = 0;
const int joySerialUpdateInterval = 2000; //send the state of the X and Y knob once a second
*/

// SCREEN DATA
int CLEAR_DISPLAY = 0;
int LINE_SELECT = 0; //can be (n*8) for n from 0 to 7
int previousScreenUpdateMillis = 0;
// For 60 FPS we want about an 18ms wait. Choose whatever lowest FPS is smoothest to reduce power usage.
const int screenUpdateWait = 18;

// GETTING TEXT DATA
const int CHARS_PER_OLED_LINE = 21;
const int textUpdateIntervalMillis = 1000;
unsigned long previousSerialTextReceivedMillis = 0;
char serialReceivedTextLine[32]; //Accept 32 bytes at a time - essentially fixed width transmissions


//SETUP
void setup() {
  // initialize serial for debug values
  Serial.begin(38400);
  
  // initialize and clear display
  display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR);
  display.clearDisplay();
  display.display();


  // display a pixel in each corner of the screen
  display.drawPixel(0, 0, WHITE);
  display.drawPixel(127, 0, WHITE);
  display.drawPixel(0, 63, WHITE);
  display.drawPixel(127, 63, WHITE);

  //Just some constant text to tell the screen is on
  //setCursor takes (X, Y)
  display.setCursor(0, 31);
  display.setTextColor(WHITE);
  display.setTextSize(1);
  display.print("Center-display text");

/*
  // Title text
  display.setCursor(8, 0);
  display.setTextColor(WHITE);
  display.setTextSize(1);
  display.print("Joystick+screen demo");
  display.display();
*/

  display.display();

}

void loop() {
  // put your main code here, to run repeatedly:
  
  // Timer for state machines to compare with
  unsigned long currentMillis = millis();
  
  
  //START OF SERIAL TEXT RECEIVING CODE
  // =============================================
  // Only check for new text at a certain interval, but try to get a full lines worth at that point
  if( currentMillis - previousSerialTextReceivedMillis > textUpdateIntervalMillis)
  {
    int i = 0; //outside loop scope so that we can add the NUL to the chararray
    int chars_available = Serial.available(); // read how many chars are available now and stick to the given number, in case more text arrives while running this code
    char curByte = 0;
    
    int lineSelect = 0;
    
    if( chars_available > 0)
    // Need at least one char ready to read
    {
      //get as many chars as will fit on one line, and also only grab chars as they are available
      for(i; (i < CHARS_PER_OLED_LINE) && chars_available > 0 ; i++)
      {
          //https://www.arduino.cc/en/Serial/Read
          curByte = Serial.read();
          //Newlines mean end of line
          if( curByte == '\n')
          {
            serialReceivedTextLine[i] = 0;
            break;
          }
          //otherwise load the byte into the string
          serialReceivedTextLine[i] = curByte;
      }
      serialReceivedTextLine[i+1] = 0;
      
      //debug - send back received text
      Serial.println();
      Serial.println(serialReceivedTextLine);
      //Important: Keep track that we just checked the serialbus for text!
      previousSerialTextReceivedMillis = currentMillis;
    }
    //Otherwise just leaves received text line as it was
    //Or, set the first char to 0 to set the line back to blank!
    else
    {
      serialReceivedTextLine[0] = 0;
    }
    //Subsection of RECEIVING code so that it runs on the same timer
    //START OF SERIAL TEXT PARSING CODE
    //==============================================
    //https://www.arduino.cc/en/Tutorial/CharacterAnalysis
      
    int commandValue = serialReceivedTextLine[0];
    if( isDigit(commandValue) )
    {
       LINE_SELECT = (commandValue - '0')*8; 
    }
    
    //'C'lear, however we want to unset this if we have not received a Clear command!
    if( commandValue == 'C' || commandValue == 'c' )
    {
       CLEAR_DISPLAY = 1;     
    }
    else
    {
       CLEAR_DISPLAY = 0; 
    }
  
  
      //END OF SERIAL TEXT PARSING CODE
      //==============================================
    
  }
  
  //END OF SERIAL TEXT RECEIVING CODE
  //==============================================

  
  //START DISPLAY CODE
  //==============================================
  //Display code - depends on joystick
  if( currentMillis - previousScreenUpdateMillis > screenUpdateWait )
  {
    previousScreenUpdateMillis = currentMillis;
    //Put our base down
    if( CLEAR_DISPLAY )
    {
      display.clearDisplay(); 
    }
    

    
    //Put the received text on the given line
    display.setCursor(0, LINE_SELECT);
    display.setTextColor(WHITE);
    display.setTextSize(1);
    display.print(serialReceivedTextLine);
    
    display.display();
  }
  
  //END OF DISPLAY CODE
  //============================================
}

