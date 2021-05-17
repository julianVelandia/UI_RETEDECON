/*
 Setup your scale and start the sketch WITHOUT a weight on the scale
 Once readings are displayed place the weight on the scale
 Press +/- or a/z to adjust the calibration_factor until the output readings match the known weight
 Arduino pin 6 -> HX711 CLK
 Arduino pin 5 -> HX711 DOUT
 Arduino pin 5V -> HX711 VCC
 Arduino pin GND -> HX711 GND 
*/

#include "HX711.h"

HX711 scale(5, 6);

float calibration_factor = 45100; // this calibration factor is adjusted according to my load cell
float units;



void setup() {
  Serial.begin(9600);
   scale.set_scale();
  scale.tare();  //Reset the scale to 0
 pinMode(LED_BUILTIN, OUTPUT);
  long zero_factor = scale.read_average(); //Get a baseline reading
 }

void loop() {

  scale.set_scale(calibration_factor); //Adjust to this calibration factor


  units = scale.get_units(), 10;
  if (units < 0)
  {
    units = 0.00;
  }

  if (units > 1)
    {
      digitalWrite(LED_BUILTIN, HIGH);
    }
  
}
