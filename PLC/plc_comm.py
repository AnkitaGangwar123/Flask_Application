"""
Modbus TCP/IP is Modbus communication transmitted over an Industrial Ethernet TCP/IP network.
"""

"""
This script will communicate with the PLC using python via Modbus Communication
and will also automatically switch the contactors.
The script is derived from modbus_data.py script
"""

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.payload import BinaryPayloadBuilder
import time 

class PLC:
    def __init__(self):
        self.SERVER_IP = '192.168.2.10'         # Modbus server IP address
        self.SERVER_PORT = 502                  # Modbus TCP port
        self.REGISTER_ADDRESS = 0x0000          # Modbus address
        self.QUANTITY = 16                      # Quantity of register to write

        self.contact_map_dict = {'c_d_1': 7,
                                 'c_d_2': 6,
                                 'c_d_3': 5,
                                 'c_d_4': 4,
                                 'c_d_5': 3,
                                 'c_d_6': 2,
                                 'c_d_7': 1,
                                 'c_d_8': 0,
                                 'smr_1': 15,
                                 'smr_2': 14,
                                 'smr_3': 13,
                                 'smr_4': 12,
                                 'smr_5': 11,
                                 'smr_6': 10,
                                 'smr_7': 9,
                                 'smr_8': 8}
        
        #byte-array is a mutable sequence that represents an array of bytes. It is similar to the 'bytes' type but allows modification of indiviual elements. 
        self.binary_data = bytearray([0x00,
                                      0x00,
                                      0x00,
                                      0x00,
                                      0x00,
                                      0x00,
                                      0x00,
                                      0x00,
                                      0x00,
                                      0x00,
                                      0x00,
                                      0x00,
                                      0x00,
                                      0x00,
                                      0x00,
                                      0x00])
        
        self.create_client()
        self.connect_client()
        
    def create_client(self):
        self.client = ModbusTcpClient(self.SERVER_IP, port=self.SERVER_PORT)
        self.client.unit_id = 1 # Set the modbus slave ID to 1

    def connect_client(self):
        self.client.connect()

    # This is the function of how to write the binary data to a holding register using Modbus TCP/IP.
    def send_payload(self):
        try:
            builder = BinaryPayloadBuilder()            # Build the binary payload
            builder.add_bits(self.binary_data)          # Add the binary data
            payload = builder.to_registers()            # Prepare the payload to be written to holding registers

            self.client.write_registers(self.REGISTER_ADDRESS, payload, unit=1, numberOfDecimals=0)

            print("Binary data successfully written to holding register 4x0001.")
        
        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Close the connection.
            self.client.close()

    def turn_on_contactor(self, contactor):
        """
        Turn ON contactor, 
        update current index based on contact mapping.
        """
        self.binary_data[self.contact_map_dict[contactor]] = 0x01
        self.send_payload()

    def turn_off_contactor(self, contactor):
        self.binary_data[self.contact_map_dict[contactor]] = 0x00
        self.send_payload()

# This will turn ON and turn OFF first three SMRs in intervals of 10 seconds each respectively. 
A = PLC()
A.turn_on_contactor('smr_1')
time.sleep(10)
A.turn_on_contactor('smr_2')
time.sleep(10)
A.turn_on_contactor('smr_3')
time.sleep(10)
A.turn_off_contactor('smr_1')
time.sleep(10)
A.turn_off_contactor('smr_2')
time.sleep(10)
A.turn_off_contactor('smr_3')

