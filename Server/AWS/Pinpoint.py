import boto3


class PinPoint():
    def __init__(self, region_name, pinpoint_phone_number):
        self.pinpoint = boto3.client("pinpoint", region_name=region_name)
        self.pinpoint_phone_number = pinpoint_phone_number

