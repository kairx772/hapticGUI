int MoPin = A5;

void setup() 
{
  pinMode(MoPin,OUTPUT);
  digitalWrite(MoPin,LOW);  
  Serial.begin(9600);
  //digitalWrite(MoPin,HIGH);
  //delay(200);
  //digitalWrite(MoPin,LOW);
}

void loop() 
{
  if(Serial.available() > 0)
  {
    if(Serial.read() == 's')
    {
      digitalWrite(MoPin,HIGH);
      delay(200);
    }
  }

    else
    {
      digitalWrite(MoPin,LOW);
    }
}
