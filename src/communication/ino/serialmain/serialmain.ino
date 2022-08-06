//////////////////////////////////SERIAL MAIN IN////////////////////////////////
////////////////////////////////////READ RFID///////////////////////////////////
#include <SPI.h>
#include <MFRC522.h>
#define RST_PIN         5             // Configurable, see typical pin layout above
#define SS_PIN          53            // Configurable, see typical pin layout above
MFRC522 mfrc522(SS_PIN, RST_PIN);     // Create MFRC522 instance

///READING DE CARD UID
void uid_array(byte *buffer, byte bufferSize) {
   for (byte i = 0; i < bufferSize; i++) {
      Serial.print(buffer[i] < 0x10 ? " 0" : " ");
      Serial.print(buffer[i], HEX);
   }
}

////////////////////////////////////IRSENSOR////////////////////////////////////
int IRSensor = 2;                     //Define the IRsensor connection

void setup() {

////////////////////////////////////READ RFID///////////////////////////////////
  Serial.begin(9600);                 // Initialize serial communications with the PC
  while (!Serial);                    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
  SPI.begin();                        // Init SPI bus
  mfrc522.PCD_Init();                 // Init MFRC522
  delay(5);                           // Optional delay.
  
////////////////////////////////////IRSENSOR////////////////////////////////////
  pinMode (IRSensor, INPUT);          //Set IRSensor digital pin 2 as INPUT

//////////////////////////////////////HC-05/////////////////////////////////////
  Serial1.begin(9600);// Initialize serial communication with the HC-05

//////////////////////////////////CELDAS DE CARGA///////////////////////////////

}

void loop() {
////////////////////////////////////IRSENSOR////////////////////////////////////
  int IRstatus = digitalRead(IRSensor);
  if (IRstatus == 0){
    String IRID = "IR"; 
    String IRBus = IRID +' '+ String(IRstatus+1);
    Serial.println(IRBus);
    delay(500);
  }else{
    String IRID = "IR"; 
    String IRBus = IRID +' '+ String(IRstatus-1);
    //Serial.println(IRBus);
    delay(500);
  }
  
//////////////////////////////////////HC-05/////////////////////////////////////
  String EXDataBus;
  if(Serial1.available() > 0){
    EXDataBus = Serial1.readString();
    Serial.println(EXDataBus);
  }
  
//////////////////////////////////CELDAS DE CARGA///////////////////////////////

////////////////////////////////////READ RFID///////////////////////////////////

  // Reset the loop if no new card present on the sensor/reader. This saves the entire process when idle.
  if (!mfrc522.PICC_IsNewCardPresent()){
    return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()){
    return;
  }
  else {
    Serial.print("IN ");  
    Serial.print(F("Card UID:"));
    uid_array(mfrc522.uid.uidByte, mfrc522.uid.size);
    Serial.println();
    // Finalizar lectura actual
    mfrc522.PICC_HaltA();
    delay(500);
  }
}
