import psutil
import wmi

class RAM():
    def __init__(self):
        self.total_ram_sticks = None
        self.total_ram_gb = None
        self.ram_speeds = None
        self.ram_usage = None
        self.stick_usage = None

        # Fetch total RAM sticks and total RAM in gigabytes
        w = wmi.WMI()
        ram_modules = w.Win32_PhysicalMemory()
        self.total_ram_sticks = len(ram_modules)
        self.total_ram_gb = psutil.virtual_memory().total / (1024 ** 3)  # Convert bytes to gigabytes

    def fetch_ram_data(self):
        # Use WMI to get detailed RAM information including RAM speed of each stick
        w = wmi.WMI()
        ram_modules = w.Win32_PhysicalMemory()
        self.ram_speeds = [int(module.ConfiguredClockSpeed) for module in ram_modules]

        # Calculate stick usage using Capacity and FreePhysicalMemory attributes
        os_info = w.Win32_OperatingSystem()[0]
        total_physical_memory = int(os_info.TotalVisibleMemorySize)
        free_physical_memory = int(os_info.FreePhysicalMemory)
        self.stick_usage = [int(module.Capacity) - free_physical_memory * 1024 for module in ram_modules]

        self.ram_usage = (total_physical_memory - free_physical_memory) / total_physical_memory * 100

    def return_ram_data(self):
        self.fetch_ram_data()

        return {
            "TotalRAMSticks": self.total_ram_sticks,
            "TotalRAMGB": self.total_ram_gb,
            "RAMSpeeds": self.ram_speeds,
            "RAMUsage": self.ram_usage,
            "StickUsage": self.stick_usage
        }

# Example usage
if __name__ == '__main__':
    ram = RAM()
    print(ram.return_ram_data())
