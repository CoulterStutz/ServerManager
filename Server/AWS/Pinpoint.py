import time
import boto3

class PinPoint():
    def __init__(self, region_name, pinpoint_application_id, destination_numbers:list):
        self.pinpoint = boto3.client("pinpoint", region_name=region_name)
        self.pinpoint_application_id = pinpoint_application_id
        self.destination_addresses = destination_numbers
        self.header_message = "This is a message from server manager! "
        self.death_message = "The following servers have gone dark! "
        self.metric_overload = "The following servers are at critical load for one or more metrics! "
        self.metric_underload = "The following servers are critically underload for one or more metrics! "

        self.message = ""

    def send_death_message(self, servers:list):
        msg = self.header_message + self.death_message + '. '.join(servers)
        self.message = msg

        self.send_message()


    def send_metric_alert(self, Isoverload:bool, metrics:dict):
        servers = []
        for server, metric in metrics.items():
            servers.append(f"{server}: {metric}")
        if Isoverload:
            msg = self.header_message + self.metric_overload + ' '.join(servers)
        else:
            msg = self.header_message + self.metric_underload + ' '.join(servers)
        self.message = msg

        self.send_message()

    def send_message(self):
        response = self.pinpoint.send_messages(
            ApplicationId=self.pinpoint_application_id,  # Replace with your Pinpoint Application ID
            MessageRequest={
                'Addresses': {
                    number: {
                        'ChannelType': 'VOICE'
                    } for number in self.destination_addresses
                },
                'MessageConfiguration': {
                    'VoiceMessage': {
                        'Body': self.message,
                        'LanguageCode': 'en',
                        'OriginationNumber': '+15014369971'
                    }
                }
            }
        )

if __name__ == "__main__":
    p = PinPoint("us-west-2", "0x00000", ['+0x000'])
    p.send_death_message(["test", "test2"])
    time.sleep(15)
    p.send_metric_alert(True, {'Test': 'CPULoad'})
    time.sleep(15)
    p.send_metric_alert(False, {'Test': 'CPULoad'})
