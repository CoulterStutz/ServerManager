import psutil

class CPU():
    def __init__(self):
        self.core_count = self.core_count = psutil.cpu_count(logical=False)
        self.cpu_usage = None
        self.core_usage = None

    def fetch_cpu_usage(self):
        self.cpu_usage = psutil.cpu_percent(interval=1)

    def fetch_core_usage(self):
        self.core_usage = psutil.cpu_percent(interval=1, percpu=True)

    def return_cpu_data(self):
        self.fetch_core_usage()
        self.fetch_cpu_usage()

        return {"CoreCount": self.core_count, "CPU Usage": self.cpu_usage, "CoreUsage": self.core_usage}

# Example usage
if __name__ == '__main__':
    c = CPU()
    print(c.return_cpu_data())
