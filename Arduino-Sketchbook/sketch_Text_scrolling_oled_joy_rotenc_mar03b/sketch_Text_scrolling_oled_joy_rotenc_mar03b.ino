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

//ROTARY ENCODER DATA
int rotary_aPin = 7; // DT pin
int rotary_bPin = 6; // CLK pin
unsigned long rotaryLastCheck = 0;
unsigned long serialLastUpdate = 0;
const int rotaryCheckInterval = 5;
const int serialUpdateInterval = 5;
int rotary_change = 0; // the last change value of the encoder
unsigned long rotaryValueResetLast = 0;
int rotary_count_buf = 0;

//PHYSICS DATA
unsigned long physTimer=0;
const int physInterval=5;
//Circle values
int centerX = 64; //calculated later on as the X of the center of the screen
int centerY = 32; //technically constant but you can make the program figure it out
int circleX = 0; //Currnet X of the circle ball
int circleY = 0;

//Paddle values (top left corner)
const int paddle_width = 6;
const int paddle_height = 25;

int LS_paddle_Y = centerY - paddle_height/2;
const int LS_paddle_X = 1;

int RS_paddle_Y = centerY - paddle_height/2;
const int RS_paddle_X = 120;

// SCREEN DATA
int previousScreenUpdateMillis = 0;
// For 60 FPS we want about an 18ms wait. Choose whatever lowest FPS is smoothest to reduce power usage.
const int screenUpdateWait = 18;

// GETTING TEXT DATA
const int CHARS_PER_OLED_LINE = 20;
const int textUpdateIntervalMillis = 1000;
unsigned long previousSerialTextReceivedMillis = 0;
char serialReceivedTextLine[CHARS_PER_OLED_LINE+1]; //enough for 29 chars and NUL

//SETUP
void setup() {
  // initialize serial for debug values
  Serial.begin(9600);
  
  // initialize and clear display
  display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR);
  display.clearDisplay();
  display.display();

/*
  // display a pixel in each corner of the screen
  display.drawPixel(0, 0, WHITE);
  display.drawPixel(127, 0, WHITE);
  display.drawPixel(0, 63, WHITE);
  display.drawPixel(127, 63, WHITE);
*/

/*
  // Title text
  display.setCursor(8, 0);
  display.setTextColor(WHITE);
  display.setTextSize(1);
  display.print("Joystick+screen demo");
  display.display();
*/
  
  // Center circle - initial
  centerX = display.width()/2;
  circleX = centerX;
  centerY = display.height()/2;
  circleY = centerY;
  display.fillCircle(centerX, centerY, 4, WHITE);
  // Black dot within the circle
  display.fillCircle(display.width()/2, display.height()/2, 2, BLACK); 
  display.display();
  
  //Set up rotary encoder pins
  pinMode (rotary_aPin, INPUT);
  pinMode (rotary_bPin, INPUT);
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
    //Serial.print("\n\nVal_y: ");
    //Serial.print(joyValue1);
    //Serial.print("\nVal_x: ");
    //Serial.print(joyValue2);
    //Serial.println(treatValue(value2));
  }
  //END OF JOYSTICK CODE
  //==============================================
  
  //ROTARY ENCODER CODE
  //==============================================
  //This block gets the status of the rotary encoder in a given interval rotaryCheckInterval (around 5ms works well)
  if( currentMillis - rotaryLastCheck > rotaryCheckInterval )
  {
    rotaryLastCheck = currentMillis;
    rotary_change = getEncoderTurn();
    // the buffer shows a general trend of the rotary movements
    rotary_count_buf += 3*rotary_change;
  }
  
  /*
  //reset rotaryChange every 50ms
  if( currentMillis - rotaryValueResetLast > 250)
  {
     rotaryValueResetLast = currentMillis;
     rotary_count_buf = 0; 
  }
  */
  
  //This block only sends the SERIAL UPDATE (basically spams the encoder's current value over serial)
  if( currentMillis - serialLastUpdate > serialUpdateInterval )
  {
    serialLastUpdate = currentMillis;
    if( rotary_change != 0 )
    {  
      Serial.print("\nRotary encoder: ");
      Serial.print(rotary_change); 
    }
  }
  //END OF ROTARY ENCODER CODE
  //==============================================
  
  //START PHYSICS CODE
  //==============================================
  //Calculate circle location and avoid leaving boundaries
  if( currentMillis - physTimer > physInterval) 
  {
    physTimer = currentMillis;
    
/*
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
*/  

    //Calculate left paddle location and avoid leaving screen
    if((rotary_count_buf < 0) && (LS_paddle_Y < (64-paddle_height))) 
    {
      LS_paddle_Y += 2;
      rotary_count_buf += 1;
    } 
    else if((rotary_count_buf > 0) && (LS_paddle_Y >= 0))
    { 
      LS_paddle_Y -= 2;
      rotary_count_buf -= 1;
    }

    //Calculate right paddle location and avoid leaving screen
    //The Y-val is 0 for the top row and INCREASES as you go down
    //So to prevent going down and out we have to check the position of the top row of the paddle is not too big
    if(joyValue1 < 450 && RS_paddle_Y <= (64-paddle_height-1)) 
    {
      RS_paddle_Y += 1; //down
    }
    //Accordingly, to prevent going up and out we have to make sure the value won't be less than 0
    else if(joyValue1 > 550 && RS_paddle_Y >= 1)
    { 
      RS_paddle_Y -= 1; //up
    }


  } 
  //END OF PHYSICS CODE
  //==============================================
  
  
  //START OF SERIAL TEXT CODE
  // =============================================
  // Only check for new text at a certain interval, but try to get a full lines worth at that point
  if( currentMillis - previousSerialTextReceivedMillis > textUpdateIntervalMillis)
  {
    int i = 0; //outside loop scope so that we can add the NUL to the chararray
    int chars_available = Serial.available(); // read how many chars are available now and stick to the given number, in case more text arrives while running this code
    char curByte = 0;
    if( chars_available > 0)
    // Need at least one char ready to read
    {
      for(i; (i < CHARS_PER_OLED_LINE) && i < chars_available ; i++)
      {
          //https://www.arduino.cc/en/Serial/Read
          curByte = Serial.read();
          // Don't want newlines to come through
          //if( curByte == '\n')
          //{
            //curByte = ' ';
          //}
          serialReceivedTextLine[i] = curByte;
      }
      serialReceivedTextLine[i+1] = 0;
      //serialReceivedTextLine[i+2] = 0;
      
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
    
  }
  
  //END OF SERIAL TEXT CODE
  //==============================================


  
  //START DISPLAY CODE
  //==============================================
  //Display code - depends on joystick
  if( currentMillis - previousScreenUpdateMillis > screenUpdateWait )
  {
    previousScreenUpdateMillis = currentMillis;
    //Put our base down
    display.clearDisplay();
/*
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
*/    
    
    // Center circle - can be moved around by joystick
    display.fillCircle(circleX, circleY, 4, WHITE);
    // Black dot within the circle
    display.fillCircle(circleX, circleY, 2, BLACK);
    //void drawRect(ui2nt16_t x0, uint16_t y0, uint16_t w, uint16_t h, uint16_t color);
    //
    
    //Draw left paddle
    display.drawRect(LS_paddle_X, LS_paddle_Y, paddle_width, paddle_height, WHITE);
    
    //Draw right paddle
    display.drawRect(RS_paddle_X, RS_paddle_Y, paddle_width, paddle_height, WHITE);
    
    //Put the received text on the top line
    display.setCursor(0, 0);
    display.setTextColor(WHITE);
    display.setTextSize(1);
    display.print(serialReceivedTextLine);
    
    display.display();
  }
  
  //END OF DISPLAY CODE
  //============================================
}

//Helper function for ROTARY ENCODER
//Reads the pins and returns the current turn value
int getEncoderTurn () { // Return -1, 0, or +1
  static int oldA = LOW;
  static int oldB = LOW;
  int result = 0;
  int newA = digitalRead (rotary_aPin);
  int newB = digitalRead (rotary_bPin);
  if (newA != oldA || newB != oldB) { // Something has changed 
    if (oldA == LOW && newA == HIGH) { result = - (oldB * 2 - 1); } 
  }
  oldA = newA;
  oldB = newB;
  return result;
}
