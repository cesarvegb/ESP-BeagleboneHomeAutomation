from bluepy.bluepy import btle
import time

service_uuid = btle.UUID("4fafc201-1fb5-459e-8fcc-c5c9c331914b") #Remote service UUID
characteristic_uuid = btle.UUID("beb5483e-36e1-4688-b7f5-ea07361b26a8") #Remote characteristic UUID

esp32_per = btle.Peripheral("80:7D:3A:A3:D9:AA") #Set a peripheral that will be connected by MAC Address

try:
    print("Success")
    services = esp32_per.getServices()
    serv = esp32_per.getServiceByUUID(service_uuid)
    charac = serv.getCharacteristics(characteristic_uuid)[0]
    if (charac.supportsRead()):
        while True:
            in_ch = charac.read()  
            print str(in_ch)
            charac.write("y",True)
            time.sleep(2000)      
except Exception as error:
    print(error)
finally:
    esp32_per.disconnect()