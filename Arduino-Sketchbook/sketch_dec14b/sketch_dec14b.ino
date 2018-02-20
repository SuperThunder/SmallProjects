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

void setup() {
  // initialize and clear display
  display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR);
  display.clearDisplay();
  display.display();

  // display a pixel in each corner of the screen
  display.drawPixel(0, 0, WHITE);
  display.drawPixel(127, 0, WHITE);
  display.drawPixel(0, 63, WHITE);
  display.drawPixel(127, 63, WHITE);

  // setup our text parameters
  display.setTextSize(1);
  display.setTextColor(WHITE);
  
  // bad horse loop
  for(int i=0; i<3; ++i)
  {
    
    display.setCursor(0, 0);
    display.print("Bad hoorse\n");
    display.display();
    delay(700);
    display.print("Bad hooorse\n");
    display.display();
    delay(700);
    display.print("Bad hooorse\n");
    display.display();
    delay(600);
    display.setTextSize(2);
    display.print("He's bad!");
    display.display();
    
    // wait for next loop
    display.setTextSize(1);
    delay(2000);
    display.clearDisplay();
    display.display();
    delay(3000);
  }
  
  
  delay(8000);
  display.setCursor(40, 16);
  display.setTextSize(4);
  display.print("<3");
  display.display();
}

void loop() {
  // put your main code here, to run repeatedly:
}

