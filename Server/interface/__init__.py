import flask
from flask import *

class Interface():
    def __init__(self, InterfaceConfig):
        self.InterfaceConfig = InterfaceConfig
        self.interface = Flask("__name__")

        self.ip = InterfaceConfig["IP"]
        self.port = InterfaceConfig["Port"]
        self.passwordAuthentication = InterfaceConfig["PasswordAuthentication"]

        self.metrics = InterfaceConfig["Metrics"]
        self.CPUMetrics = self.metrics["AWSCPUMetricsLink"]
        self.CPUMetrics = self.metrics["AWSStorageMetricsLink"]
        self.CPUMetrics = self.metrics["AWSNetworkMetricsLink"]
        self.CPUMetrics = self.metrics["AWSRamMetricsLink"]
        self.custom_metrics = self.metrics["CustomMetrics"]

        @self.interface.route("/")
        def index():
            return flask.render_template("index")

        @self.interface.route("/metrics")
        def metrics():
            return flask.render_template("metrics")

    def run(self):
        self.interface.run(self.host, self.port)