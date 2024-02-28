import psutil

class RAM():
    def __init__(self):
        self.total_ram_gb = None
        self.ram_usage = None

        # Fetch total RAM in gigabytes
        self.total_ram_gb = psutil.virtual_memory().total / (1024 ** 3)  # Convert bytes to gigabytes

    def fetch_ram_data(self):
        # Use psutil to get RAM usage
        self.ram_usage = psutil.virtual_memory().percent

    def return_ram_data(self):
        self.fetch_ram_data()

        return {
            "TotalRAMGB": self.total_ram_gb,
            "RAMUsage": self.ram_usage
        }

# Example usage
if __name__ == '__main__':
    ram = RAM()
    print(ram.return_ram_data())
