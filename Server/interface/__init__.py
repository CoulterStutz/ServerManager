from flask import *

class Interface():
    def __init__(self, InterfaceConfig):
        self.InterfaceConfig = InterfaceConfig

        self.ip = InterfaceConfig["IP"]
        self.port = InterfaceConfig["Port"]
        self.passwordAuthentication = InterfaceConfig["PasswordAuthentication"]
        self.metrics = InterfaceConfig["Metrics"]

        self.CPUMetrics = self.metrics["AWSCPUMetricsLink"]
        self.CPUMetrics = self.metrics["AWSStorageMetricsLink"]
        self.CPUMetrics = self.metrics["AWSNetworkMetricsLink"]
        self.CPUMetrics = self.metrics["AWSRamMetricsLink"]

        self.custom_metrics = self.metrics["CustomMetrics"]