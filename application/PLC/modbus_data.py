"""
This script will communicate with the PLC using python via Modbus Communication
and will also manually switch the contactors.
"""

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.payload import BinaryPayloadBuilder

# Modbus TCP/IP server configurations
SERVER_IP = '192.168.2.10'  # Change this to your server's IP address
SERVER_PORT = 502  # Default Modbus TCP port

# Address of the register you want to write binary data to (Modbus address 4x0001)
REGISTER_ADDRESS = 0x0000  # Modbus address is zero-based

# Quantity of registers to write
QUANTITY = 16

# Binary data you want to write (example: byte array)
binary_data = bytearray([0x00,          # C/D contactor channel 1
                         0x00,          # C/D contactor channel 2
                         0x01,          # C/D contactor channel 3
                         0x00,          # C/D contactor channel 4
                         0x00,          # C/D contactor channel 5
                         0x00,          # C/D contactor channel 6
                         0x00,          # C/D contactor channel 7
                         0x00,          # C/D contactor channel 8
                         0x00,          # SMR contactor channel 1
                         0x00,          # SMR contactor channel 2
                         0x01,          # SMR contactor channel 3
                         0x00,          # SMR contactor channel 4
                         0x00,          # SMR contactor channel 5
                         0x00,          # SMR contactor channel 6
                         0x01,          # SMR contactor channel 7
                         0x00])         # SMR contactor channel 8

print(binary_data)

# Create a Modbus TCP client with specific slave ID
client = ModbusTcpClient(SERVER_IP, port=SERVER_PORT)
client.unit_id = 1  # Set the Modbus slave ID to 1

# Connect to the Modbus TCP server
client.connect()

try:
    # Build the binary payload
    builder = BinaryPayloadBuilder()
    builder.add_bits(binary_data)  # Add the binary data

    # Prepare the payload to be written to holding registers
    payload = builder.to_registers()  # Writing to holding registers

    # Write the binary data to the specified holding registers (Modbus address 4x0001)
    client.write_registers(REGISTER_ADDRESS, payload, unit=1, numberOfDecimals=0)

    print("Binary data successfully written to holding register 4x0001.")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    client.close()
