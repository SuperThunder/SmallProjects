// stripped down from http://innov8maui.com/files/Sunfounder37kit/RotaryEncoder.html
// the bare minimum code to get the info on the rotary encoder turning


int aPin = 7; // DT pin
int bPin = 6; // CLK pin
unsigned long rotaryLastCheck = 0;
unsigned long serialLastUpdate = 0;

const int rotaryCheckInterval = 5;
const int serialUpdateInterval = 5;

int change = 0; // the last change value of the encoer

void setup () {
  pinMode (aPin, INPUT);
  pinMode (bPin, INPUT);
  
  Serial.begin(9600);
  Serial.print("Rotary encoder test");
}
void loop ()
{
  unsigned long currentMillis = millis();

  if( currentMillis - rotaryLastCheck > rotaryCheckInterval )
  {
    rotaryLastCheck = currentMillis;
    
    change = getEncoderTurn ();
  }
  
  if( currentMillis - serialLastUpdate > serialUpdateInterval )
  {
    serialLastUpdate = currentMillis;
    if( change != 0 )
    {   
      Serial.println(change); 
    }
  }
}

int getEncoderTurn () { // Return -1, 0, or +1
  static int oldA = LOW;
  static int oldB = LOW;
  int result = 0;
  int newA = digitalRead (aPin);
  int newB = digitalRead (bPin);
  if (newA != oldA || newB != oldB) { // Something has changed 
    if (oldA == LOW && newA == HIGH) { result = - (oldB * 2 - 1); } 
  }
  oldA = newA;
  oldB = newB;
  return result;
}
