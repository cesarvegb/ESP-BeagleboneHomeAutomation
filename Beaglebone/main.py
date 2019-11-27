from bluepy.bluepy import btle
import bleconnection as bt
import time

ble = bt.BLE_Connection()

try:
    ble.connect()
    print("Success")
    ble.get_service()
    temp_humid = ble.get_characteristics(ble.temp_hummid_uuid)
    lightmeter = ble.get_characteristics(ble.lightmeter_uuid)
    pir = ble.get_characteristics(ble.pir_char_uuid)
    ldr = ble.get_characteristics(ble.ldr_char_uuid)

    if (temp_humid.supportsRead()):
        while True:
            in_ch = temp_humid.read()  
            print str(in_ch)
            temp_humid.write("y",True)
            time.sleep(2000)      
except Exception as error:
    print(error)
finally:
    esp32_per.disconnect()