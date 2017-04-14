/*------------ESP8266 WiFi------------------*/
#include <SoftwareSerial.h>
SoftwareSerial module(5,6); //RX , TX

 /*--------------------DHT11 Humidity------------------------*/
#include <dht.h>
dht DHT;
#define DHT11_PIN 7


 /*--------------------DS18B20 Temperature -------------------*/
#include <OneWire.h>
#include <DallasTemperature.h> 
#define ONE_WIRE_BUS 4
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

/*--------------------MFRC522 RFID----------------------------*/
#include <MFRC522.h>
#include <SPI.h>
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);

/*--------------------HX711 Weight Sensor---------------------*/
#include "HX711.h"  
#define DOUT  3
#define CLK 2
HX711 scale(DOUT, CLK);
float calibration_factor = -116270.00;

String s;
unsigned long a;


void setup(void){
  Serial.begin(115200);
  while(!Serial){
    ;
  }
  module.begin(115200);
  while(!module){
    ;
  }
  module.print("+++");
  Serial.println("ESP8266 Demo");
  delay(5000);
  module.println("AT");
  delay(1000);
  if(module.find("OK")){
    Serial.println("Module Ready");
  }

  module.println("AT+CWQAP");
  if(module.find("OK")){
    Serial.println("No connection. Establishing one.");
  }

  int f=0;
  while(f==0){
    module.println("AT+CWJAP=\"Moto G (4) 8350\",\"shravi27\"");
    delay(2000);
    if(module.find("OK")){
      Serial.println("Connected To Wifi.");
      f=1;
    }
  }
  f=0;
  while(f==0){
    module.println("AT+CIPSTART=\"TCP\",\"192.168.43.98\",8080");
    if(module.find("OK")){
      Serial.println("Connection Setup.");
      f=1;
    }
  }

  module.println("AT+CIPMODE=1");
  delay(100);
  module.println("AT+CIPSEND");
  delay(100);


  sensors.begin();   //For DS18B20 Temperature Sensor

 
 SPI.begin();      // Init SPI bus
 mfrc522.PCD_Init(); // Init MFRC522 card
 Serial.println("Scan PICC to see UID and type...");

  
 Serial.println("Press T to tare");
 scale.set_scale(-116270.00);  //Calibration Factor obtained from first sketch
 scale.tare(); //Reset the scale to 0  

 a=0;
}

void sendData(String hVal){
  String c = "GET /api/store/";
  c+=hVal;
  c+="\n";
  module.println(c);
  module.flush();

}

/*--------------------MFRC522 RFID----------------------------*/
unsigned long rfidVal(){
  unsigned long hex_num=a;
 
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }

  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }
  
  
  hex_num =  mfrc522.uid.uidByte[0] << 24;
  hex_num += mfrc522.uid.uidByte[1] << 16;
  hex_num += mfrc522.uid.uidByte[2] <<  8;
  hex_num += mfrc522.uid.uidByte[3];
  mfrc522.PICC_HaltA();
  a = hex_num;
  return hex_num;
  
}

String fin(void) {
  s="";

   /*--------------------DS18B20 Temperature -------------------*/
  sensors.requestTemperatures(); 
  s=s+sensors.getTempCByIndex(0)+"_";
  
  /*--------------------DHT11 Humidity------------------------*/
   int chk = DHT.read11(DHT11_PIN);
   s=s+DHT.humidity+"_";

  /*--------------------HX711 Weight Sensor---------------------*/

  if(Serial.available())
  {
    char temp = Serial.read();
    if(temp == 't' || temp == 'T')
    {
      scale.tare();  //Reset the scale to zero
    }
            
  }
  s=s+scale.get_units()+"_";
  
 
  /*--------------------MFRC522 RFID----------------------------*/
  
  s=s+rfidVal();

  //Serial.println(s);

  delay(1000);

  return s;
 
}

void loop(void){
  sendData(fin());
//    if(Serial.available()>0){
//    while(Serial.available()>0){
//      char rbyte = Serial.read();
//      module.print(rbyte);
//      Serial.print(rbyte); 
//    }
//  }
//
//  if(module.available()>0){
//    while(module.available()>0){
//      char rbyte = module.read();
//      Serial.print(rbyte); 
//    }
//  }
}

