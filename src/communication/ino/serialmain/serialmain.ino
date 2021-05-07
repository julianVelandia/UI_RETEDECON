////////////////////////////////////////////////////////////////////////////////
#include <SPI.h>
#include <MFRC522.h>
#include <SoftwareSerial.h>
#define RST_PIN         9             // Configurable, see typical pin layout above
#define SS_PIN          10            // Configurable, see typical pin layout above
MFRC522 mfrc522(SS_PIN, RST_PIN);     // Create MFRC522 instance
SoftwareSerial mySerial(7, 8);        // RX, TX
int IRSensor = 2;                     //Define the IRsensor connection

void setup() {
  /////////////////READ RFID///////////////////
  Serial.begin(9600);                 // Initialize serial communications with the PC
  while (!Serial);                    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
  SPI.begin();                        // Init SPI bus
  mfrc522.PCD_Init();                 // Init MFRC522
  delay(5);                           // Optional delay. Some board do need more time after init to be ready, see Readme
  mfrc522.PCD_DumpVersionToSerial();  // Show details of PCD - MFRC522 Card Reader details
  
  /////////////////IRSENSOR///////////////////
  pinMode (IRSensor, INPUT);          //Set IRSensor digital pin 2 as INPUT

  ///////////////////HC-05///////////////////
  mySerial.begin(9600);               // Initialize serial communication with the HC-05
}

void loop() {
  ///////////////IRSENSOR////////////////////////
  int IRstatus = digitalRead(IRSensor);
  if (IRstatus == 0){
    String IRID = "IR"; 
    String IRBus = IRID +' '+ String(IRstatus+1);
    Serial.println(IRBus);
    delay(1000);
  }else{
    String IRID = "IR"; 
    String IRBus = IRID +' '+ String(IRstatus-1);
    //Serial.println(IRBus);
    delay(1000);
  }
  
  ///////////////////HC-05///////////////////
  String EXDataBus;
  if(mySerial.available() > 0){
    EXDataBus = mySerial.read();
    Serial.println(EXDataBus);
  }
  
  /////////////////READ RFID///////////////////
  // Reset the loop if no new card present on the sensor/reader. This saves the entire process when idle.
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }
  // Dump debug info about the card; PICC_HaltA() is automatically called
  mfrc522.PICC_DumpToSerial(&(mfrc522.uid));

}
