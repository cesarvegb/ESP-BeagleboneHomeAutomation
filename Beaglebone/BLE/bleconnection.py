# Functions to connect

from bluepy.bluepy import btle
import bleconfig

class BLE_Connection:
        def __init__(self):
            self.addr = DEV_ADDR
            self.serv_uuid = btle.UUID(SERVICE_UUID)         # Remote service UUID
            self.temp_uuid = btle.UUID(TEMP_UUID)            # Remote characteristic UUID
            self.hummid_uuid = btle.UUID(HUM_UUID)
            self.lightmeter_uuid = btle.UUID(LIGHT_UUID)     # Lightmeter characteristic UUID
            self.pir_char_uuid = btle.UUID(PIR_UUID)         # PIR characteristic UUID
            self.ldr_char_uuid = btle.UUID(LDR_UUID)         # LDR characteristic UUID
            self.con = btle.Peripheral(self.addr)    # Set a peripheral that will be connected by MAC Address

        def connect(self):
            self.servs = self.con.getServices()

        def get_service(self):
            self.serv = self.con.getServiceByUUID(self.serv_uuid)

        def get_characteristics(self,uuid):
            return self.serv.getCharacteristics(uuid)[0]


