"""
This script will activate the server.
"""

from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext

def run_modbus_server():
    # Define the Modbus datastore (holding register)
    print("Setting up Modbus datastore.")
    store = ModbusSlaveContext(
        di = ModbusSequentialDataBlock(0, [0]*100),  # Discrete Inputs
        co = ModbusSequentialDataBlock(0, [0]*100),  # Coils
        hr = ModbusSequentialDataBlock(0, [0]*100),  # Holding Registers
        ir = ModbusSequentialDataBlock(0, [0]*100)   # Input Registers
    )
    context = ModbusServerContext(slaves=store, single=True)

    print("Starting Modbus TCP Server on 192.168.2.10:502")
    try:
        server = StartTcpServer(context, address=("192.168.2.10", 502))
        server.serve_forever()
    except Exception as e:
        print(f"Failed to start server: {e}")
    except KeyboardInterrupt:
        print("Shutting down server.")
    finally:
        print("Server stopped.")

run_modbus_server()

