#include <DHT.h>
#include <WiFi.h>
#include <LiquidCrystal_I2C.h>
#define DHTTYPE DHT11 
#define DHTPIN 15
LiquidCrystal_I2C LCD1(0x27,16,2);
DHT dht(DHTPIN, DHTTYPE);
String apiKey = "xxxxxxxxxxx"; // Enter your Write API key from ThingSpeak
const char* ssid = "Jasmine";
const char* password = "123456";
const char* server = "api.thingspeak.com";
float h,t,f;
int co,nh3,so2;
float ico,inh3,iso2;
const int co_pin = 13;
const int nh3_pin = 27;
const int so2_pin = 14;

WiFiClient client;
 
void setup()
{
  Serial.begin(115200);
  Serial.println("Connecting To ");
  Serial.println(ssid);
  dht.begin();
  LCD1.init();
  LCD1.backlight();
  LCD1.clear();
  
  //connect to your local wi-fi network
  WiFi.begin(ssid, password);
  LCD1.setCursor(0,0);
  LCD1.print("Connecting->WiFi");
  LCD1.setCursor(0,1);
  //check wi-fi is connected to wi-fi network
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
    LCD1.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected..!");
  Serial.print("Got IP: ");
  Serial.println(WiFi.localIP());
  LCD1.clear();
  LCD1.setCursor(0,0);
  LCD1.print("WiFi Connected");
  pinMode(co_pin,INPUT);pinMode(so2_pin,INPUT);pinMode(nh3_pin,INPUT);
  delay(1000);
 
}
 
void loop()
{
  Serial.println("**********Air Quality System**********");
  LCD1.clear();
  LCD1.setCursor(0,0);  LCD1.print("**Air Quality**");
  LCD1.setCursor(0,1);  LCD1.print("  ***System***");
  delay(1500);
  if (isnan(h) || isnan(t) || isnan(f)) 
  {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  Serial.print("Humidity=");Serial.print(h);Serial.println("%");
  Serial.print("Temperature=");Serial.print(t);Serial.println("°C");
  LCD1.clear();
  LCD1.setCursor(0,0);  LCD1.print(" Temp   Humidity");
  LCD1.setCursor(0,1);  LCD1.print(t);LCD1.print("*C  ");LCD1.print(h);LCD1.print("%"); 
  delay(2000);
  co = digitalRead(co_pin);
  if(co==HIGH)
 {
  Serial.println("CO Gas not present");
  LCD1.clear();  LCD1.setCursor(0,0);  LCD1.print("CO Not Present");
  ico=0;
 }
 else
 {
  Serial.println("CO Gas Is Present");
  LCD1.clear();  LCD1.setCursor(0,0);  LCD1.print("CO Present");
  ico=1;
 }
 delay(2000);
 nh3 = digitalRead(nh3_pin);
  if(nh3==HIGH)
 {
  Serial.println("NH3 Gas not present");
  LCD1.clear();  LCD1.setCursor(0,0);  LCD1.print("NH3 Not Present");
  inh3=0;
 }
 else
 {
  Serial.println("NH3 Gas Is Present");
  LCD1.clear();  LCD1.setCursor(0,0);  LCD1.print("NH3 Present");
  inh3=1;
 }
 delay(2000);
 so2 = digitalRead(so2_pin);
  if(so2==HIGH)
 {
  Serial.println("SO2 Gas not present");
  LCD1.clear();  LCD1.setCursor(0,0);  LCD1.print("SO2 Not Present");
  iso2=0;
 }
 else
 {
  Serial.println("SO2 Gas Is Present");
  LCD1.clear();  LCD1.setCursor(0,0);  LCD1.print("SO2 Present");
  iso2=1;
 }
delay(2000);
  if (client.connect(server, 80)) // "184.106.153.149" or api.thingspeak.com
  {
    String postStr = apiKey;
    postStr += "&field1=";
    postStr += String(h);
    postStr += "&field2=";
    postStr += String(t);
    postStr += "&field3=";
    postStr += String(ico);  
    postStr += "&field4=";
    postStr += String(inh3);
    postStr += "&field5=";
    postStr += String(iso2);
    postStr += "\r\n";

    client.print("POST /update HTTP/1.1\n");
    client.print("Host: api.thingspeak.com\n");
    client.print("Connection: close\n");
    client.print("X-THINGSPEAKAPIKEY: " + apiKey + "\n");
    client.print("Content-Type: application/x-www-form-urlencoded\n");
    client.print("Content-Length: ");
    client.print(postStr.length());
    client.print("\n\n");
    client.print(postStr);

    Serial.println("Data Send to Thingspeak");  
    LCD1.clear();
    LCD1.setCursor(0,0);  LCD1.print("DATA UPLOADED");
    LCD1.setCursor(0,1);  LCD1.print("TO THINGSPEAK");
    delay(2000);
  }
  client.stop();
  Serial.println("******************************************");
}
