#include <Arduino.h>
#include <stdlib.h>
#include <sstream>
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>

// See the following for generating UUIDs:
// https://www.uuidgenerator.net/

#define SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"

//static uint8_t  SERVICE_UUID_BIN[] = {0x4f, 0xaf, 0xc2, 0x01, 0x1f, 0xb5, 0x45, 0x9e, 0x8f, 0xcc, 0xc5, 0xc9, 0xc3, 0x31, 0x91, 0x4b};


class MyCallback: public BLECharacteristicCallbacks {
  
  int c = 0;
	void onRead(BLECharacteristic *pCharacteristic) {
    c++;
    std::stringstream st;
    st << c;
		pCharacteristic->setValue(st.str());
	}
  void onWrite(BLECharacteristic *pCharacteristic) {
    std::string value = pCharacteristic->getValue();
		if (value.length() > 0) {
        Serial.println();
				Serial.print("New data received: ");
        for (int i = 0; i < value.length();i++)
          Serial.print(value[i]);
        Serial.println();
		}
  }
};


void setup() {
  Serial.begin(9600);
  Serial.println("Starting BLE work!");

  BLEDevice::init("ESPPecera");
  BLEServer *pServer = BLEDevice::createServer();
  BLEService *pService = pServer->createService(BLEUUID(SERVICE_UUID));
  BLECharacteristic *pCharacteristic = pService->createCharacteristic(
    CHARACTERISTIC_UUID,
    BLECharacteristic::PROPERTY_READ |
    BLECharacteristic::PROPERTY_WRITE
  );
  // BLEAdvertising *pAdvertising = pServer->getAdvertising();  // this still is working for backward compatibility
  pCharacteristic->setCallbacks(new MyCallback);
  pCharacteristic->setValue("ESP aqui");
  pService->start();
  BLEAdvertising *pAdvertising = pServer->getAdvertising();
  pAdvertising->start();

  Serial.println(pCharacteristic->getValue()[0]);
}

void loop() {
  // put your main code here, to run repeatedly: 
  delay(2000);
}