import datetime

from .cpu import CPU
from .storage import Storage
from .network import Network
from .mem import RAM
from .gpu import GPU
from .temps import SystemTemperatures
import json

class DataManager():
    def __init__(self):
        self.cpu_manager = CPU()
        self.storage_manager = Storage()
        self.network_manager = Network()
        self.ram_manager = RAM()
        self.gpu_manager = GPU()
        self.temps_manager = SystemTemperatures()

    def get_all_data(self):
        cpu_data = self.cpu_manager.return_cpu_data()
        storage_data = self.storage_manager.return_storage_data()
        network_data = self.network_manager.return_network_data()
        ram_data = self.ram_manager.return_ram_data()
        gpu_data = self.gpu_manager.return_gpu_data()
        temps_data = self.temps_manager.get_storage_temp()

        data = {
            "CPUData": cpu_data,
            "StorageData": storage_data,
            "NetworkData": network_data,
            "RAMData": ram_data,
            "GPUData": gpu_data,
            "Temps": temps_data
        }

        return data

    def return_data_json(self):
        return json.dumps(self.get_all_data(), indent=4)