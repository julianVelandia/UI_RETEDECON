////////////////////////////////////////////////////////////////////////////////
#include <SPI.h>
#include <MFRC522.h>
//#include <SoftwareSerial.h>
#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN          10         // Configurable, see typical pin layout above
MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance
//SoftwareSerial mySerial(7, 8); // RX, TX
String EXDataBus;

void setup() {

  /////////////////READ RFID///////////////////
  Serial.begin(9600);                 // Initialize serial communications with the PC
  while (!Serial);                    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
  SPI.begin();                        // Init SPI bus
  mfrc522.PCD_Init();                 // Init MFRC522
  delay(5);                           // Optional delay. Some board do need more time after init to be ready, see Readme
  mfrc522.PCD_DumpVersionToSerial();  // Show details of PCD - MFRC522 Card Reader details

  /////////////////HC-05//////////////////////
  //mySerial.begin(9600);               // Initialize serial communication with the HC-05
}

void loop() {
 
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
  //mfrc522.PICC_DumpToSerial(&(mfrc522.uid));
  String bus;
  for (byte i = 0; i < mfrc522.uid.size; i++) {
          Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
          bus = String(mfrc522.uid.uidByte[i]);
  }
  Serial.println(bus);
/////////////HC-05////////////////////
  //if (mfrc522.PICC_IsNewCardPresent()){
    //EXDataBus = mfrc522.PICC_ReadCardSerial();
    //mySerial.println(EXDataBus);
  //}
  
}
