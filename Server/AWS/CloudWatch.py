import boto3

class CloudWatch():
    def __init__(self, region):
        self.client = boto3.client("cloudwatch", region_name=region)

    def report_metric(self, server, data):
        # CPU Metrics
        for core, usage in enumerate(data['CPUData']['CoreUsage'], 1):
            self.client.put_metric_data(
                Namespace="ServerManager",
                MetricData=[
                    {
                        'MetricName': f'CPU{core}Usage',
                        'Dimensions': [
                            {
                                'Name': 'Server',
                                'Value': server
                            },
                        ],
                        'Unit': 'Percent',
                        'Value': usage
                    },
                ]
            )

        # Storage Metrics
        self.cloudwatch.put_metric_data(
            Namespace="",
            MetricData=[
                {
                    'MetricName': 'StorageTotalFree',
                    'Dimensions': [
                        {
                            'Name': 'Server',
                            'Value': server
                        },
                    ],
                    'Unit': 'Bytes',
                    'Value': data['StorageData']['TotalFreeStorage']
                },
                {
                    'MetricName': 'StorageTotalUsed',
                    'Dimensions': [
                        {
                            'Name': 'Server',
                            'Value': server
                        },
                    ],
                    'Unit': 'Bytes',
                    'Value': data['StorageData']['TotalUsedStorage']
                },
            ]
        )

        # Network Metrics
        self.cloudwatch.put_metric_data(
            Namespace=self.namespace,
            MetricData=[
                {
                    'MetricName': 'NetworkTotalPacketsIn',
                    'Dimensions': [
                        {
                            'Name': 'Server',
                            'Value': server
                        },
                    ],
                    'Unit': 'Count',
                    'Value': data['NetworkData']['TotalPacketsInAllInterfaces']
                },
                {
                    'MetricName': 'NetworkTotalPacketsOut',
                    'Dimensions': [
                        {
                            'Name': 'Server',
                            'Value': server
                        },
                    ],
                    'Unit': 'Count',
                    'Value': data['NetworkData']['TotalPacketsOutAllInterfaces']
                },
            ]
        )

        # RAM Metrics
        self.cloudwatch.put_metric_data(
            Namespace=self.namespace,
            MetricData=[
                {
                    'MetricName': 'RAMUsage',
                    'Dimensions': [
                        {
                            'Name': 'Server',
                            'Value': server
                        },
                    ],
                    'Unit': 'Percent',
                    'Value': data['RAMData']['RAMUsage']
                },
            ]
        )