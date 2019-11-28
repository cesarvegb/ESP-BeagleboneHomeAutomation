from bluepy.bluepy import btle
import bleconnection as bt
import time

ble = bt.BLE_Connection()

try:
    ble.connect()
    print("Success")
    ble.get_service()
    temp = ble.get_characteristics(ble.temp_uuid)
    hummid = ble.get_characteristics(ble.hummid_uuid)
    lightmeter = ble.get_characteristics(ble.lightmeter_uuid)
    pir = ble.get_characteristics(ble.pir_char_uuid)
    ldr = ble.get_characteristics(ble.ldr_char_uuid)

    while True:
        if (temp.supportsRead()):
            in_ch = temp.read()  
            print str(in_ch)
            temp.write("A",True)
            time.sleep(1)
        else:
            break

        if (hummid.supportsRead()):
            in_ch = hummid.read()  
            print str(in_ch)
            hummid.write("A",True)
            time.sleep(1)
        else:
            break
        
        if (lightmeter.supportsRead()):
            in_ch = lightmeter.read()  
            print str(in_ch)
            lightmeter.write("B",True)
            time.sleep(1)
        else:
            break

        if (pir.supportsRead()):
            in_ch = pir.read()  
            print str(in_ch)
            pir.write("A",True)
            time.sleep(1)
        else:
            break

        if (ldr.supportsRead()):
            in_ch = ldr.read()  
            print str(in_ch)
            ldr.write("B",True)
            time.sleep(1)
        else:
            break
             
except Exception as error:
    print(error)
finally:
    esp32_per.disconnect()