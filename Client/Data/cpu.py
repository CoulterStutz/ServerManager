import psutil

class CPU():
    def __init__(self):
        self.cpu_name = None
        self.core_count = None
        self.cpu_usage = None
        self.core_usage = None
        self.cpu_temp = None
        self.core_temp = None

    def fetch_cpu_data(self):
        self.core_count = psutil.cpu_count(logical=False)
        self.cpu_usage = psutil.cpu_percent(interval=1)
        self.core_usage = psutil.cpu_percent(interval=1, percpu=True)
        self.cpu_temp = self.fetch_cpu_temp()
        self.core_temp = [self.fetch_core_temp(core) for core in range(self.core_count)]

    def fetch_cpu_temp(self):
        try:
            temps = psutil.sensors_temperatures()
            if "coretemp" in temps:
                coretemp = temps["coretemp"]
                for entry in coretemp:
                    if "Package id 0" in entry.label:
                        return entry.current
        except Exception as e:
            print(f"Failed to fetch CPU temperature: {e}")
        return None

    def fetch_core_temp(self, core):
        try:
            temps = psutil.sensors_temperatures()
            if "coretemp" in temps:
                coretemp = temps["coretemp"]
                for entry in coretemp:
                    if f"Core {core}" in entry.label:
                        return entry.current
        except Exception as e:
            print(f"Failed to fetch core temperature for core {core}: {e}")
        return None

# Example usage
if __name__ == '__main__':
    cpu = CPU()
    cpu.fetch_cpu_data()
    print(cpu.cpu_name)
    print(cpu.core_count)
    print(cpu.cpu_usage)
    print(cpu.core_usage)
    print(cpu.cpu_temp)
    print(cpu.core_temp)