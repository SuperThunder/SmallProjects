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

  // display a line of text
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(27,30);
  display.print("This is a somewhat long sentence!");
  
  display.setCursor(5, 10);
  display.setTextSize(2);
  display.print("00TEST00");
  
  // update display with all of the above graphics
  display.display();
  
  // let the first bit of stuff show for a second
  delay(1000);
  // draw a white circle, 10 pixel radius
  for(int i=0; i<30; i++){
    display.fillCircle(display.width()/2, display.height()/2, i, WHITE);
    delay(75);
    display.display();
  }
  delay(1000);
  
  display.clearDisplay();
  display.display(); //clearDisplay() just clears "our version", still need to push that update out
  delay(1000);
  
  display.setCursor(40, 16);
  display.setTextSize(4);
  display.print("<3");
  display.display();
}

void loop() {
  // put your main code here, to run repeatedly:
}

