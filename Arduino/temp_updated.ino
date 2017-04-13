#include <OneWire.h>
#include <DallasTemperature.h>
 
#define ONE_WIRE_BUS 3
OneWire oneWire(ONE_WIRE_BUS);
 
DallasTemperature sensors(&oneWire);
 
void setup(void)
{
  Serial.begin(9600);
    sensors.begin();
}
 
 
void loop(void)
{
  sensors.requestTemperatures(); 
  // Send the command to get temperatures
  Serial.print(sensors.getTempCByIndex(0));

}
