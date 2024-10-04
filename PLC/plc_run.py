"""
This script will place the PLC in run mode automatically without opening the Siemens PLC software.
snap7 library is for Siemens PLCs using the S7 protocol.
"""

import snap7

def enable_run_mode(ip_address):
    try:
        # Create a connection to the PLC
        plc = snap7.client.Client()
        # Rack number refers to the physical housing where the main CPU of the PLC is located. If connecting directly to the PLC's CPU module, then the rack number is 0.
        # Slot number refers to the slot position within the rack where the CPU or modules are installed.
        # Unlike large Siemens PLCs like S7-300 or S7-400 series, S7-200 operates without the concept of racks and slots.
        plc.connect(ip_address, 0, 2)  # Adjust rack and slot numbers if needed

        # Switch PLC to RUN mode
        plc.set_run()

        # Close the connection
        plc.disconnect()
        print("Successfully enabled RUN mode on Siemens PLC at", ip_address)
    except snap7.snap7exceptions.Snap7Exception as e:
        print("Snap7Exception:", e)
    except Exception as ex:
        print("An error occurred:", ex)

# Replace '192.168.2.1' with the IP address of your Siemens PLC
plc_ip_address = '192.168.2.1'

try:
    enable_run_mode(plc_ip_address)
except Exception as e:
    print("An error occurred:", e)

