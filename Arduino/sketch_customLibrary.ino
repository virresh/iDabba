#include <SoftwareSerial.h>

SoftwareSerial module(5,6); //RX , TX

void setup(){
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
    module.println("AT+CWJAP=\"CC\",\"c0dechamps\"");
    delay(2000);
    if(module.find("OK")){
      Serial.println("Connected To Wifi.");
      f=1;
    }
  }
  f=0;
  while(f==0){
    module.println("AT+CIPSTART=\"TCP\",\"192.168.43.54\",8080");
    if(module.find("OK")){
      Serial.println("Connection Setup.");
      f=1;
    }
  }

  module.println("AT+CIPMODE=1");
  delay(100);
  module.println("AT+CIPSEND");
  delay(100);
  
}

void sendData(String hVal){
//  module.println("AT+CIPSTART=\"TCP\",\"192.168.43.54\",8080");
//  delay(1000);
  String c = "GET /api/store/";
  c+=hVal;
  c+="\n";
  module.println(c);
  module.flush();
//  module.print("\n");
//  delay(100);
//  module.print("+++");
//  delay(10);
//  module.println("AT");
//  if(module.find("OK")){
//    Serial.println("Transmission ended.");
//  }
//  module.println("AT+CIPCLOSE");
//  delay(100);
}


void loop(){
//  if(Serial.available()>0){
//    while(Serial.available()>0){
//      char rbyte = Serial.read();
//      module.print(rbyte);
////      Serial.print(rbyte); 
//    }
//  }
//
//  if(module.available()>0){
//    while(module.available()>0){
//      char rbyte = module.read();
//      Serial.print(rbyte); 
//    }
//  }

//  int chk = DHT.read11(DHT11_PIN);
//  Serial.print("Humidity = ");
  sendData("Bla_Bla_Bla_Bla_Bla");
//  Serial.println(DHT.humidity);
//  delay(10000);
}
