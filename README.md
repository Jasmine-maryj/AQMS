# AQMS

This project implements the air quality monitoring system based on state-of-art Internet Of Things techniques. In this system, portable sensors collect air quality information timely and the ambient temperature and humidity. It will display the sensed data in a user-friendly format on an LCD and Thing Speak Cloud.

## Pre-requisites 

### Software Requirements
  1. ThingSpeak IOT Cloud
  2. Arduino IDE
  3. Libraries
     -> Sensors Libraries such as DHT.h, WiFi.h, and LiquidCrystal_I2C.h
     -> Machine Learning libraries such as numpy, pandas, matplotlib, seaborn, tkinter, sqlite3
  4. Visual Studio Code

### Hardware Requirements
  1. Temperature and Humidity Sensors
  2. WiFi Module
  3. LCD
  4. Jump Wires
  5. Power Cables

## Build and Installation
1. Install and download Arduino IDE, then download all the sensor libraries in Arduino IDE
2. Since we are using ESP32, select esp32 board
3. Download POM3 and add it to the Driver Manager if you don't have one. Select port and add POM3 port.
4. Configure WiFi password and ThingSpeak IOT Cloud channel key.
