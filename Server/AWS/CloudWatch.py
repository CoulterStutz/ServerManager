import boto3
import json

class CloudWatchManager:
    def __init__(self):
        self.cloudwatch = boto3.client('cloudwatch')

    def report_metric(self, server, data):
        # CPU Metrics
        total_cpu_usage = sum(data['CPUData']['CoreUsage'])
        self.cloudwatch.put_metric_data(
            Namespace=f'ServerManager/{server}/CPU',
            MetricData=[
                {
                    'MetricName': 'TotalUsage',
                    'Unit': 'Percent',
                    'Value': total_cpu_usage
                },
            ]
        )

        for core, usage in enumerate(data['CPUData']['CoreUsage'], 1):
            self.cloudwatch.put_metric_data(
                Namespace=f'ServerManager/{server}/CPU/{core}',
                MetricData=[
                    {
                        'MetricName': 'Usage',
                        'Unit': 'Percent',
                        'Value': usage
                    },
                ]
            )

        # Storage Metrics
        for i, drive in enumerate(data['StorageData']['DrivesFreeStorage'], 1):
            self.cloudwatch.put_metric_data(
                Namespace=f'ServerManager/{server}/Storage/Drive{i}',
                MetricData=[
                    {
                        'MetricName': 'FreeStorage',
                        'Unit': 'Bytes',
                        'Value': drive
                    },
                ]
            )

        # Network Metrics
        for interface, status in data['NetworkData']['LinkStatus'].items():
            self.cloudwatch.put_metric_data(
                Namespace=f'ServerManager/{server}/Network/Interface/{interface}',
                MetricData=[
                    {
                        'MetricName': 'LinkStatus',
                        'Value': 1 if status else 0
                    },
                ]
            )

        # RAM Metrics
        self.cloudwatch.put_metric_data(
            Namespace=f'ServerManager/{server}/RAM',
            MetricData=[
                {
                    'MetricName': 'Usage',
                    'Unit': 'Percent',
                    'Value': data['RAMData']['RAMUsage']
                },
            ]
        )

# Example usage
cloudwatch_manager = CloudWatchManager()
data = {...}  # Your server data
cloudwatch_manager.report_metric('TestServer1', data)
