import psutil

class Storage():
    def __init__(self):
        self.read_time = None
        self.write_time = None
        self.partitions = psutil.disk_partitions(all=False)
        self.drive_count = len(self.partitions)
        self.total_free_storage = None
        self.total_used_storage = None
        self.drives_free_storage = None
        self.drives_used_storage = None
        self.drives_write_operations = None
        self.drives_read_operations = None
        self.drive_write_bytes = None
        self.drive_read_bytes = None

    def fetch_drive_data(self):
        partitions = psutil.disk_partitions(all=False)
        self.drive_count = len(partitions)
        self.total_free_storage = sum(psutil.disk_usage(part.mountpoint).free for part in partitions)
        self.total_used_storage = sum(psutil.disk_usage(part.mountpoint).used for part in partitions)
        self.drives_free_storage = [psutil.disk_usage(part.mountpoint).free for part in partitions]
        self.drives_used_storage = [psutil.disk_usage(part.mountpoint).used for part in partitions]
        disk_io_counters = psutil.disk_io_counters(perdisk=True)

        self.drives_write_operations = []
        self.drives_read_operations = []
        self.drive_write_bytes = []
        self.drive_read_bytes = []
        #self.write_time = []
        #self.read_time = []

        for x in disk_io_counters:
            self.drives_read_operations.append(disk_io_counters[x][0])
            self.drives_write_operations.append(disk_io_counters[x][1])
            self.drive_read_bytes.append(disk_io_counters[x][2])
            self.drive_write_bytes.append(disk_io_counters[x][3])

            #self.read_time.append(disk_io_counters[x][4])
            #self.write_time.append(disk_io_counters[x][5])

            print()


    def return_storage_data(self):
        self.fetch_drive_data()

        return {
            "DriveCount": self.drive_count,
            "TotalFreeStorage": self.total_free_storage,
            "TotalUsedStorage": self.total_used_storage,
            "DrivesFreeStorage": self.drives_free_storage,
            "DrivesUsedStorage": self.drives_used_storage,
            "DrivesWriteOperations": self.drives_write_operations,
            "DrivesReadOperations": self.drives_read_operations,
            "DrivesWriteBytes": self.drive_write_bytes,
            "DrivesReadBytes": self.drive_read_bytes
        }

# Example usage
if __name__ == '__main__':
    storage = Storage()
    print(storage.return_storage_data())
