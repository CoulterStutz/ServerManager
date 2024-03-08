import psutil
import GPUtil

class GPU():
    def __init__(self):
        self.gpu_count = len(GPUtil.getGPUs())
        self.gpu_usage = None
        self.memory_usage = None

    def fetch_gpu_usage(self):
        gpus = GPUtil.getGPUs()
        self.gpu_usage = [gpu.load * 100 for gpu in gpus]
        self.memory_usage = [gpu.memoryUsed / (1024**3) for gpu in gpus]

    def return_gpu_data(self):
        self.fetch_gpu_usage()

        return {"GPUCount": self.gpu_count, "GPUUsage": self.gpu_usage, "MemoryUsage": self.memory_usage}

# Example usage
if __name__ == '__main__':
    g = GPU()
    print(g.return_gpu_data())
