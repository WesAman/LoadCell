#include <SD.h>  // Include the SD library
#include <SoftwareSerial.h>  // Include the SoftwareSerial library

// Define the analog input pin for the force transducer
#define FORCE_PIN A0

// Define the serial port for the datalogger
SoftwareSerial dataLogger(10, 11);  // RX, TX

void setup() {
  // Initialize the serial port for debugging
  Serial.begin(9600);
  
  // Initialize the SD card
  SD.begin(4);

  // Initialize the datalogger serial port
  dataLogger.begin(9600);

  // Write the CSV header to the file
  File dataFile = SD.open("force_data.csv", FILE_WRITE);
  if (dataFile) {
    dataFile.println("Force (kg),Time (s)");
    dataFile.close();
  } else {
    Serial.println("Error opening file");
  }
}

void loop() {
  // Read the force value from the transducer
  int forceRaw = analogRead(FORCE_PIN);
  
  // Convert the force value to kilograms
  float forceKg = map(forceRaw, 0, 1023, 0, 100) / 9.81;

  // Get the current time in seconds
  unsigned long currentTime = millis();
  float timeSec = (float)currentTime / 1000.0;

  // Write the force and time values to the serial port
  Serial.print("Force (kg): ");
  Serial.print(forceKg);
  Serial.print(", Time (s): ");
  Serial.println(timeSec);

  // Write the force and time values to the CSV file
  File dataFile = SD.open("force_data.csv", FILE_WRITE);
  if (dataFile) {
    dataFile.print(forceKg);
    dataFile.print(",");
    dataFile.println(timeSec);
    dataFile.close();
  } else {
    Serial.println("Error opening file");
  }

  // Delay for 100ms
  delay(100);
}
