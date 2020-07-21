#include <SPI.h>
#include <MFRC522.h>

#define RST A0
#define SS  10

MFRC522 mf(SS, RST);

void setup(){
  Serial.begin(9600);
  SPI.begin();
  mf.PCD_Init();
  Serial.println("Ready");
}

void loop(){
  if(mf.PICC_IsNewCardPresent() && mf.PICC_ReadCardSerial()){
    byte* id = mf.uid.uidByte;
    byte idSize = mf.uid.size;

    for(byte i = 0; i < idSize; ++i){
      if(id[i] < 0x10)Serial.print('0');
      Serial.print(id[i], HEX);
    }
    Serial.println();
    mf.PICC_HaltA();
  }
}
