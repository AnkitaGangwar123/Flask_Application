import cantools
import time
from can import Message
from can.interfaces.ixxat import IXXATBus, exceptions

class pack_can_data:
    def __init__(self, baudrate):
        self.baudrate = baudrate
        self.bus = None
        self.can_command = Message(is_extended_id=False,
                                   arbitration_id=0x77F,
                                   dlc=0x08,
                                   data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        
        self.cycle_time = time.time() + 5
        self.message = []
        self.data_dict = {}             #instance to store can data
        self.parameters = []            #List for appending battery parameters
        self.cell_voltages = []         #List for appending cell voltages
        self.cell_temperatures = []     #List for appending cell temperatures
        self.errors_events = []         #List for appending errors and events
        self.can_bus()

        self.decoded_data = {}
        # self.database_file()
    
    def can_bus(self):
        self.bus = IXXATBus(channel=0,
                            can_filters=[{"can_id": 0x00, "can_mask": 0x00}],
                            bitrate = self.baudrate)

    def read_can_message(self):
        self.message = self.bus.recv()
        self.decode_message()
        return self.decoded_data
    
    def database_file(self, filepath):
        self.database = cantools.database.load_file(filepath)
        self.iterate_messages()

    def iterate_messages(self):
        for message in self.database.messages:
            # Battery parameters
            if message.name in ["BMS_MSG_11_SID", "BMS_MSG_10_SID", "BMS_MSG_03_SID", "BMS_MSG_02_EID"]:
                for signal in message.signals:
                    self.parameters.append(signal.name)
            # Cell voltages 
            if message.name in ["BMS_MSG_CV0104_EID", "BMS_MSG_CV0508_EID", "BMS_MSG_CV0912_EID","BMS_MSG_CV1316_EID"]:
                for signal in message.signals:
                    self.cell_voltages.append(signal.name)
            # Cell temperatures 
            if message.name in ["BMS_MSG_CT0003_SID", "BMS_MSG_CT0407_SID"]:
                for signal in message.signals:
                    self.cell_temperatures.append(signal.name)
            # Errors and Warnings
            if message.name in ["BMS_MSG_13_SID"]:
                for signal in message.signals:
                    self.errors_events.append(signal.name)

            # Keeping all the parameters in the dictionary      
            for signal in message.signals:
                self.data_dict[signal.name] = ''

    def decode_message(self):
        try:
            self.decoded_data = self.database.decode_message(self.message.arbitration_id, self.message.data)
        except:
            pass
    
    def send_cyclic_message(self, message):
        self.cycle_time = time.time() + 1
        #self.bus.send(message)
        self.bus.send(message, timeout = 2)

    def charging_enable_command(self):
        command = Message(is_extended_id=False,
                          arbitration_id=0x77F,
                          dlc=0x08,
                          data=[0x84,
                                0x08,
                                0x01,
                                0x00,
                                0x00,
                                0x00,
                                0x00,
                                0x00])
        
        self.send_cyclic_message(command)

    def charging_disable_command(self):
        command = Message(is_extended_id=False,
                          arbitration_id=0x77F,
                          dlc=0x08,
                          data=[0x84,
                                0x08,
                                0x00,
                                0x00,
                                0x00,
                                0x00,
                                0x00,
                                0x00])
        
        self.send_cyclic_message(command)
