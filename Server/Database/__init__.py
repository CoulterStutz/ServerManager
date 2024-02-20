import sqlite3
import json

class RegistryDB:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
                            id INTEGER PRIMARY KEY,
                            server_name, TEXT,
                            cpu_core_count INTEGER,
                            cpu_usage REAL,
                            cpu_core_usage TEXT,
                            storage_drive_count INTEGER,
                            storage_total_free_storage BIGINT,
                            storage_total_used_storage BIGINT,
                            storage_drives_free_storage TEXT,
                            storage_drives_used_storage TEXT,
                            storage_drives_processing TEXT,
                            network_total_interface_count INTEGER,
                            network_interfaces TEXT,
                            network_link_status TEXT,
                            network_packets_in_total TEXT,
                            network_packets_out_total TEXT,
                            network_total_packets_in_all_interfaces BIGINT,
                            network_total_packets_out_all_interfaces BIGINT,
                            network_packets_in_last_second TEXT,
                            network_packets_out_last_second TEXT,
                            ram_total_ram_sticks INTEGER,
                            ram_total_ram_gb INTEGER,
                            ram_speeds TEXT,
                            ram_ram_usage REAL,
                            ram_stick_usage REAL
                        )''')
        self.conn.commit()

    def clear_table(self):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM my_table')
        self.conn.commit()

    def write_data(self, server_name, data):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO my_table (
                            server_name, cpu_core_count, cpu_usage, cpu_core_usage,
                            storage_drive_count, storage_total_free_storage, storage_total_used_storage,
                            storage_drives_free_storage, storage_drives_used_storage, storage_drives_processing,
                            network_total_interface_count, network_interfaces, network_link_status,
                            network_packets_in_total, network_packets_out_total,
                            network_total_packets_in_all_interfaces, network_total_packets_out_all_interfaces,
                            network_packets_in_last_second, network_packets_out_last_second,
                            ram_total_ram_sticks, ram_total_ram_gb, ram_speeds, ram_ram_usage, ram_stick_usage
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (server_name, data['CPUData']['CoreCount'], data['CPUData']['CPU Usage'], json.dumps(data['CPUData']['CoreUsage']),
                         data['StorageData']['DriveCount'], data['StorageData']['TotalFreeStorage'], data['StorageData']['TotalUsedStorage'],
                         json.dumps(data['StorageData']['DrivesFreeStorage']), json.dumps(data['StorageData']['DrivesUsedStorage']),
                         json.dumps(data['StorageData']['DrivesProcessing']), data['NetworkData']['TotalInterfaceCount'],
                         json.dumps(data['NetworkData']['Interfaces']), json.dumps(data['NetworkData']['LinkStatus']),
                         json.dumps(data['NetworkData']['PacketsInTotal']), json.dumps(data['NetworkData']['PacketsOutTotal']),
                         data['NetworkData']['TotalPacketsInAllInterfaces'], data['NetworkData']['TotalPacketsOutAllInterfaces'],
                         json.dumps(data['NetworkData']['PacketsInLastSecond']), json.dumps(data['NetworkData']['PacketsOutLastSecond']),
                         data['RAMData']['TotalRAMSticks'], data['RAMData']['TotalRAMGB'], json.dumps(data['RAMData']['RAMSpeeds']),
                         data['RAMData']['RAMUsage'], data['RAMData']['StickUsage']))
        self.conn.commit()

# Example usage
if __name__ == '__main__':
    db = MyDatabase('my_database.db')
    db.clear_table()  # Uncomment this line if you want to clear the table on initialization

    # Example data to write to the database
    data = [{'CPUData': {'CoreCount': 4, 'CPU Usage': 7.7, 'CoreUsage': [24.6, 7.8, 20.3, 15.6, 18.8, 14.1, 18.8, 17.2]},
             'StorageData': {'DriveCount': 1, 'TotalFreeStorage': 107753574400, 'TotalUsedStorage': 398712823808,
                             'DrivesFreeStorage': [107753574400], 'DrivesUsedStorage': [398712823808],
                             'DrivesProcessing': [[15975337, 5890347, 213078607872, 172760509440, 4219, 2253]]},
             'NetworkData': {'TotalInterfaceCount': 6,
                             'Interfaces': {'Ethernet': [True, 2, 1000, 1500, ''],
                                            'Ethernet 3': [True, 2, 100, 1500, ''],
                                            'Ethernet 4': [True, 2, 100, 1500, ''],
                                            'Ethernet 2': [True, 2, 1000, 1500, ''],
                                            'Ethernet 5': [False, 2, 1000, 1500, ''],
                                            'Loopback Pseudo-Interface 1': [True, 2, 1073, 1500, '']},
                             'LinkStatus': {'Ethernet': True, 'Ethernet 3': True, 'Ethernet 4': True,
                                            'Ethernet 2': True, 'Ethernet 5': False, 'Loopback Pseudo-Interface 1': True},
                             'PacketsInTotal': {'Ethernet': 239985923, 'Ethernet 3': 0, 'Ethernet 4': 0,
                                                 'Ethernet 2': 0, 'Ethernet 5': 0, 'Loopback Pseudo-Interface 1': 0},
                             'PacketsOutTotal': {'Ethernet': 37869565, 'Ethernet 3': 1397, 'Ethernet 4': 1426,
                                                  'Ethernet 2': 0, 'Ethernet 5': 0, 'Loopback Pseudo-Interface 1': 0},
                             'TotalPacketsInAllInterfaces': 239985923, 'TotalPacketsOutAllInterfaces': 37872388,
                             'PacketsInLastSecond': {'Ethernet': 239986529, 'Ethernet 3': 0, 'Ethernet 4': 0,
                                                     'Ethernet 2': 0, 'Ethernet 5': 0, 'Loopback Pseudo-Interface 1': 0},
                             'PacketsOutLastSecond': {'Ethernet': 37869890, 'Ethernet 3': 1397, 'Ethernet 4': 1426,
                                                      'Ethernet 2': 0, 'Ethernet 5': 0, 'Loopback Pseudo-Interface 1': 0}},
             'RAMData': {'TotalRAMSticks': 0, 'TotalRAMGB': 0, 'RAMSpeeds': None, 'RAMUsage': 0, 'StickUsage': 0}},
            {'CPUData': {'CoreCount': 4, 'CPU Usage': 17.2, 'CoreUsage': [34.8, 15.6, 28.1, 21.9, 20.0, 17.2, 23.4, 26.6]},
             'StorageData': {'DriveCount': 1, 'TotalFreeStorage': 107753336832, 'TotalUsedStorage': 398713061376,
                             'DrivesFreeStorage': [107753336832], 'DrivesUsedStorage': [398713061376],
                             'DrivesProcessing': [[15975338, 5890399, 213078611968, 172761062912, 4219, 2253]]},
             'NetworkData': {'TotalInterfaceCount': 6,
                             'Interfaces': {'Ethernet': [True, 2, 1000, 1500, ''],
                                            'Ethernet 3': [True, 2, 100, 1500, ''],
                                            'Ethernet 4': [True, 2, 100, 1500, ''],
                                            'Ethernet 2': [True, 2, 1000, 1500, ''],
                                            'Ethernet 5': [False, 2, 1000, 1500, ''],
                                            'Loopback Pseudo-Interface 1': [True, 2, 1073, 1500, '']},
                             'LinkStatus': {'Ethernet': True, 'Ethernet 3': True, 'Ethernet 4': True,
                                            'Ethernet 2': True, 'Ethernet 5': False, 'Loopback Pseudo-Interface 1': True},
                             'PacketsInTotal': {'Ethernet': 239988707, 'Ethernet 3': 0, 'Ethernet 4': 0,
                                                 'Ethernet 2': 0, 'Ethernet 5': 0, 'Loopback Pseudo-Interface 1': 0},
                             'PacketsOutTotal': {'Ethernet': 37890685, 'Ethernet 3': 1397, 'Ethernet 4': 1426,
                                                  'Ethernet 2': 0, 'Ethernet 5': 0, 'Loopback Pseudo-Interface 1': 0},
                             'TotalPacketsInAllInterfaces': 239988707, 'TotalPacketsOutAllInterfaces': 37893508,
                             'PacketsInLastSecond': {'Ethernet': 239988707, 'Ethernet 3': 0, 'Ethernet 4': 0,
                                                     'Ethernet 2': 0, 'Ethernet 5': 0, 'Loopback Pseudo-Interface 1': 0},
                             'PacketsOutLastSecond': {'Ethernet': 37890740, 'Ethernet 3': 1397, 'Ethernet 4': 1426,
                                                      'Ethernet 2': 0, 'Ethernet 5': 0, 'Loopback Pseudo-Interface 1': 0}},
             'RAMData': {'TotalRAMSticks': 0, 'TotalRAMGB': 0, 'RAMSpeeds': None, 'RAMUsage': 0, 'StickUsage': 0}}]

    for item in data:
        db.write_data(item)
