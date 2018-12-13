//node 0 = mega
#include "DHT.h"
#define DHTPIN 53
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

String PC = "";
String readStringBT, readStringPC;
float temp0, hum0;

void setup() {
  Serial.begin(9600);
  Serial1.begin(9600);
  dht.begin();
}

void loop() {
  /*
    while (Serial.available()) {                //BACA DATA DARI SERIAL PC
    delay(10);
    readStringPC += char(Serial.read());
    }
  */

  temp0 = dht.readTemperature();
  hum0 = dht.readHumidity();
  
  while (Serial1.available()) {                //BACA DATA DARI SERIAL BT
    delay(10);
    readStringBT += char(Serial1.read());
  }
  if (readStringBT != 0) {
    Serial.println(readStringBT);
    Serial.println(temp0);
    Serial.println(hum0);
    Serial.println();
    readStringBT = "";
    delay(80);
    Serial1.print(temp0);
    Serial1.print("X");
    Serial1.print(hum0);
    Serial1.print("X");
    delay(80);
  }

  /*
    if (readStringPC.length() > 0) {
    BT.println(readStringPC);
    readStringPC = "";
    }
  */
}

/*
void serialEvent() {
  while (Serial.available()) {
    PC += Serial.read();

    if (PC != 0) {
      PC = "";
      delay(80);
      Serial.print('HEAD'); //HEAD
      Serial.print("X");
      Serial.print(temp1);
      Serial.print("X");
      Serial.print(temp2);
      Serial.print("X");
      Serial.print(temp3);
      Serial.print("X");
      Serial.print(hum1);
      Serial.print("X");
      Serial.print(hum2);
      Serial.print("X");
      Serial.print(hum3);
      Serial.println("X");
      delay(80);
    }
  }
}
*/

