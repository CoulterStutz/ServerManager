import boto3

class CloudWatch():
    def __init__(self, region):
        self.client = boto3.client("cloudwatch", region_name=region)

    def report_data(self, server):
        None