import psutil


class Storage():
    def __init__(self):
        self.partitions = psutil.disk_partitions(all=False)
        self.drive_count = len(self.partitions)
        self.total_free_storage = None
        self.total_used_storage = None
        self.drives_free_storage = None
        self.drives_used_storage = None
        self.drives_processing = None

    def fetch_drive_data(self):
        partitions = psutil.disk_partitions(all=False)
        self.drive_count = len(partitions)
        self.total_free_storage = sum(psutil.disk_usage(part.mountpoint).free for part in partitions)
        self.total_used_storage = sum(psutil.disk_usage(part.mountpoint).used for part in partitions)
        self.drives_free_storage = [psutil.disk_usage(part.mountpoint).free for part in partitions]
        self.drives_used_storage = [psutil.disk_usage(part.mountpoint).used for part in partitions]
        self.drives_processing = [psutil.disk_io_counters(perdisk=True)[drive] for drive in psutil.disk_io_counters(perdisk=True)]

    def return_storage_data(self):
        self.fetch_drive_data()

        return {"DriveCount": self.drive_count, "TotalFreeStorage": self.total_free_storage, "TotalUsedStorage": self.total_used_storage,
                "DrivesFreeStorage": self.drives_free_storage, "DrivesUsedStorage": self.drives_used_storage, "DrivesProcessing": self.drives_processing}

# Example usage
if __name__ == '__main__':
    storage = Storage()
    print(storage.return_storage_data())