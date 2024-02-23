import boto3

class CloudWatch():
    def __init__(self, region):
        self.cloudwatch = boto3.client("cloudwatch", region_name=region)

    def report_metric(self, server, data):
        # CPU Metrics
        total_cpu_usage = sum(data['CPUData']['CoreUsage'])
        self.cloudwatch.put_metric_data(
            Namespace=f'ServerManager/CPU',
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
                Namespace=f'ServerManager/coreCPU',
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
                Namespace=f'ServerManager/Storage',
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
                Namespace=f'ServerManager/Network',
                MetricData=[
                    {
                        'MetricName': 'LinkStatus',
                        'Value': 1 if status else 0
                    },
                ]
            )

        # RAM Metrics
        self.cloudwatch.put_metric_data(
            Namespace=f'ServerManager/RAM',
            MetricData=[
                {
                    'MetricName': 'Usage',
                    'Unit': 'Percent',
                    'Value': data['RAMData']['RAMUsage']
                },
            ]
        )