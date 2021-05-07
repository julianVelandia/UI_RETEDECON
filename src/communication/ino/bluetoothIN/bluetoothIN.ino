#include <SoftwareSerial.h>

SoftwareSerial mySerial(8, 9); // RX, TX

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  mySerial.begin(38400);
  while(!Serial){;}
  Serial.println("config");
}

void loop() { // run over and over
  if (mySerial.available())
    Serial.write(mySerial.read());
  if (Serial.available()) 
    mySerial.write(Serial.read());
}
