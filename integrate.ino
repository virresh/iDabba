#include <dht.h>
dht DHT;
#define DHT11_PIN 7
#include <MFRC522.h>
#include <SPI.h>
#include <MFRC522.h>
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);
#include <OneWire.h>
#include <DallasTemperature.h> 
#define ONE_WIRE_BUS 3
OneWire oneWire(ONE_WIRE_BUS);
 
DallasTemperature sensors(&oneWire);
 
void setup(void)
{
  Serial.begin(9600);
  sensors.begin();
  SPI.begin();      // Init SPI bus
  mfrc522.PCD_Init(); // Init MFRC522 card
  Serial.println("Scan PICC to see UID and type...");
}
 
 
void loop(void)
{
  //Temperature Sensor
  sensors.requestTemperatures(); 
  // Send the command to get temperatures
  Serial.print(sensors.getTempCByIndex(0));

  //Humidity Sensor
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("Humidity = ");
  Serial.println(DHT.humidity);

  //RFID sensor
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }

  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  // Dump debug info about the card. PICC_HaltA() is automatically called.
  mfrc522.PICC_DumpToSerial(&(mfrc522.uid));

  delay(2000);
}


