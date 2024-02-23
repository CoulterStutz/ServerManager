import boto3

class CloudWatch:
    def __init__(self, region):
        self.cloudwatch = boto3.client("cloudwatch", region_name=region)

    def report_metric(self, server, data, minimal=False):
        # CPU Metrics
        total_cpu_usage = data["CPUData"]["CPU Usage"]
        self.cloudwatch.put_metric_data(
            Namespace=f'ServerManager/CPU',
            MetricData=[
                {
                    'MetricName': 'TotalUsage',
                    'Dimensions': [
                        {
                            'Name': server,
                            'Value': 'Server'
                        },
                    ],
                    'Unit': 'Percent',
                    'Value': total_cpu_usage
                },
            ]
        )

        if not minimal:
            for core, usage in enumerate(data['CPUData']['CoreUsage'], 1):
                self.cloudwatch.put_metric_data(
                    Namespace=f'ServerManager/CPU',
                    MetricData=[
                        {
                            'MetricName': f'Core{core}',
                            'Dimensions': [
                                {
                                    'Name': server,
                                    'Value': 'Server'
                                },
                            ],
                            'Unit': 'Percent',
                            'Value': usage
                        },
                    ]
                )

        # Storage Metrics

        self.cloudwatch.put_metric_data(
            Namespace=f'ServerManager/Storage',
            MetricData=[
                {
                    'MetricName': f'TotalFreeStorage',
                    'Dimensions': [
                        {
                            'Name': server,
                            'Value': 'Server'
                        },
                    ],
                    'Unit': 'Bytes',
                    'Value': data['StorageData']['TotalFreeStorage']
                },
            ]
        )

        self.cloudwatch.put_metric_data(
            Namespace=f'ServerManager/Storage',
            MetricData=[
                {
                    'MetricName': f'TotalUsedStorage',
                    'Dimensions': [
                        {
                            'Name': server,
                            'Value': 'Server'
                        },
                    ],
                    'Unit': 'Bytes',
                    'Value': data['StorageData']['TotalUsedStorage']
                },
            ]
        )

        self.cloudwatch.put_metric_data(
            Namespace=f'ServerManager/Storage',
            MetricData=[
                {
                    'MetricName': f'TotalDriveCount',
                    'Dimensions': [
                        {
                            'Name': server,
                            'Value': 'Server'
                        },
                    ],
                    'Unit': 'Count',
                    'Value': data['StorageData']['DriveCount']
                },
            ]
        )

        if not minimal:
            for i, drive in enumerate(data['StorageData']['DrivesFreeStorage'], 1):
                self.cloudwatch.put_metric_data(
                    Namespace=f'ServerManager/Storage',
                    MetricData=[
                        {
                            'MetricName': f'FreeStorageDrive{i}',
                            'Dimensions': [
                                {
                                    'Name': server,
                                    'Value': 'Server'
                                },
                            ],
                            'Unit': 'Bytes',
                            'Value': drive
                        },
                    ]
                )

            for i, drive in enumerate(data['StorageData']['DrivesUsedStorage'], 1):
                self.cloudwatch.put_metric_data(
                    Namespace=f'ServerManager/Storage',
                    MetricData=[
                        {
                            'MetricName': f'UsedStorageDrive{i}',
                            'Dimensions': [
                                {
                                    'Name': server,
                                    'Value': 'Server'
                                },
                            ],
                            'Unit': 'Bytes',
                            'Value': drive
                        },
                    ]
                )

                for i, drive in enumerate(data['StorageData']['DrivesWriteOperations'], 1):
                    self.cloudwatch.put_metric_data(
                        Namespace=f'ServerManager/Storage',
                        MetricData=[
                            {
                                'MetricName': f'DrivesWriteOperations{i}',
                                'Dimensions': [
                                    {
                                        'Name': server,
                                        'Value': 'Server'
                                    },
                                ],
                                'Unit': 'Count',
                                'Value': data['StorageData']['DrivesWriteOperations'][drive]
                            },
                        ]
                    )

                    for i, drive in enumerate(data['StorageData']['DrivesReadOperations'], 1):
                        self.cloudwatch.put_metric_data(
                            Namespace=f'ServerManager/Storage',
                            MetricData=[
                                {
                                    'MetricName': f'DrivesReadOperations{i}',
                                    'Dimensions': [
                                        {
                                            'Name': server,
                                            'Value': 'Server'
                                        },
                                    ],
                                    'Unit': 'Count',
                                    'Value': data['StorageData']['DrivesWriteOperations'][drive]
                                },
                            ]
                        )

                    for i, drive in enumerate(data['StorageData']['DriveReadBytes'], 1):
                        self.cloudwatch.put_metric_data(
                            Namespace=f'ServerManager/Storage',
                            MetricData=[
                                {
                                    'MetricName': f'DriveReadBytes{i}',
                                    'Dimensions': [
                                        {
                                            'Name': server,
                                            'Value': 'Server'
                                        },
                                    ],
                                    'Unit': 'Bytes',
                                    'Value': data['StorageData']['DrivesWriteOperations'][drive]
                                },
                            ]
                        )

                        for i, drive in enumerate(data['StorageData']['DriveWriteBytes'], 1):
                            self.cloudwatch.put_metric_data(
                                Namespace=f'ServerManager/Storage',
                                MetricData=[
                                    {
                                        'MetricName': f'DriveWriteBytes{i}',
                                        'Dimensions': [
                                            {
                                                'Name': server,
                                                'Value': 'Server'
                                            },
                                        ],
                                        'Unit': 'Bytes',
                                        'Value': data['StorageData']['DrivesWriteOperations'][drive]
                                    },
                                ]
                            )

        # Network Metrics
        for interface, status in data['NetworkData']['LinkStatus'].items():
            self.cloudwatch.put_metric_data(
                Namespace=f'ServerManager/Network',
                MetricData=[
                    {
                        'MetricName': f'LinkStatus_{interface}',
                        'Dimensions': [
                            {
                                'Name': server,
                                'Value': 'Server'
                            },
                        ],
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
                    'Dimensions': [
                        {
                            'Name': server,
                            'Value': 'Server'
                        },
                    ],
                    'Unit': 'Percent',
                    'Value': data['RAMData']['RAMUsage']
                },
            ]
        )
