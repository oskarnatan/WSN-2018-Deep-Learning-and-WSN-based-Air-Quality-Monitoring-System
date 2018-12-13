//node 2 = UNO2
#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

#include <SoftwareSerial.h>
SoftwareSerial BT(10, 11); // RX, TX

String PC = "";
String readStringBT, readStringPC;
float temp2, hum2;

void setup() {
  Serial.begin(9600);
  BT.begin(9600);
  dht.begin();
}

void loop() {
  /*
    while (Serial.available()) {                //BACA DATA DARI SERIAL PC
    delay(10);
    readStringPC += char(Serial.read());
    }
  */
  temp2 = dht.readTemperature();
  hum2 = dht.readHumidity();
  
  while (BT.available()) {                //BACA DATA DARI SERIAL BT
    delay(10);
    readStringBT += char(BT.read());
  }
  if (readStringBT != 0) {
    Serial.println(readStringBT);
    Serial.println(temp2);
    Serial.println(hum2);
    Serial.println();
    readStringBT = "";
    delay(80);
    BT.print(temp2);
    BT.print("X");
    BT.print(hum2);
    BT.println("X");
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
