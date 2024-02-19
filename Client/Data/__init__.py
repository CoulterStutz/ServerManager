from .cpu import CPU
from .storage import Storage
from .network import Network
from .mem import RAM
import json

class DataManager():
    def __init__(self):
        self.cpu_manager = CPU()
        self.storage_manager = Storage()
        self.network_manager = Network()
        self.ram_manager = RAM()

    def get_all_data(self):
        cpu_data = self.cpu_manager.return_cpu_data()
        storage_data = self.storage_manager.return_storage_data()
        network_data = self.network_manager.return_network_data()
        ram_data = self.ram_manager.return_ram_data()

        return {
            "CPUData": cpu_data,
            "StorageData": storage_data,
            "NetworkData": network_data,
            "RAMData": ram_data
        }

    def return_data_json(self):
        return json.dumps(self.get_all_data(), indent=4)