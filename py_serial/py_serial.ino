#include <Wire.h>
#include "Adafruit_DRV2605.h"

int MoPin = 6;
const int S=225;
char cmd;

void setup() 
{
  pinMode(MoPin,OUTPUT);
  digitalWrite(MoPin,LOW);  
  Serial.begin(115200);
  //digitalWrite(MoPin,HIGH);
  //delay(200);
  //digitalWrite(MoPin,LOW);
}
uint8_t effect = 1;
void loop() 
{
  if(Serial.available() > 0)
  {
    cmd = Serial.read();
    if(cmd == 's')
    {
      digitalWrite(MoPin,HIGH);
    }
    else if(cmd == 'q')
    {
      digitalWrite(MoPin,LOW);
    }
    else if(cmd == 'w') 
    {
      digitalWrite(MoPin,HIGH);
      delayMicroseconds(700);
      //delay(1);
      digitalWrite(MoPin,LOW);
    }
    else if(cmd == 'd') 
    {
      digitalWrite(MoPin,HIGH);
      delay(10);
      //delay(1);
      digitalWrite(MoPin,LOW);
    }
  }


}
