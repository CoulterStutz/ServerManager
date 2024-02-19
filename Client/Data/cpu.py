import psutil

class CPU():
    def __init__(self):
        self.core_count = None
        self.cpu_usage = None
        self.core_usage = None

    def fetch_core_count(self):
        self.core_count = psutil.cpu_count(logical=False)

    def fetch_cpu_usage(self):
        self.cpu_usage = psutil.cpu_percent(interval=1)

    def fetch_core_usage(self):
        self.core_usage = psutil.cpu_percent(interval=1, percpu=True)

# Example usage
if __name__ == '__main__':
    cpu = CPU()
    cpu.fetch_core_count()
    cpu.fetch_cpu_usage()
    cpu.fetch_core_usage()
    print(cpu.core_count)
    print(cpu.cpu_usage)
    print(cpu.core_usage)
