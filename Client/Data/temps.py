import psutil
import GPUtil
import os

class SystemTemperatures():
    def __init__(self):
        pass

    def get_cpu_temp(self):
        try:
            temps = psutil.sensors_temperatures()
            if 'coretemp' in temps:
                core_temps = temps['coretemp']
                avg_temp = sum([temp.current for temp in core_temps]) / len(core_temps)
                return avg_temp
        except Exception as e:
            print(f"Error getting CPU temperature: {e}")
        return None

    def get_gpu_temp(self):
        try:
            gpus = GPUtil.getGPUs()
            gpu_temps = [gpu.temperature for gpu in gpus]
            return gpu_temps
        except Exception as e:
            print(f"Error getting GPU temperature: {e}")
        return None

    def get_storage_temp(self):
        try:
            if os.name == 'posix':
                # Linux command to get temperature for first storage device (may need to adjust for your system)
                return os.popen("sudo hddtemp /dev/sda").readline().strip()
            elif os.name == 'nt':
                # Windows command to get temperature for first storage device (may need to adjust for your system)
                return os.popen("wmic diskdrive get temperature").readline().strip()
        except Exception as e:
            print(f"Error getting storage temperature: {e}")
        return None

    def get_system_temperatures(self):
        cpu_temp = self.get_cpu_temp()
        gpu_temp = self.get_gpu_temp()
        storage_temp = self.get_storage_temp()
        return {"CPU Temp": cpu_temp, "GPU Temp": gpu_temp, "Storage Temp": storage_temp}

# Example usage
if __name__ == '__main__':
    st = SystemTemperatures()
    print(st.get_system_temperatures())
