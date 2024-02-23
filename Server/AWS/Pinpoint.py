import boto3


class PinPoint():
    def __init__(self, region_name, pinpoint_application_id):
        self.pinpoint = boto3.client("pinpoint", region_name=region_name)
        self.pinpoint_application_id = pinpoint_application_id



    def call(self, destination_number, servers:list):
        response = self.pinpoint.send_messages(
            ApplicationId=self.pinpoint_application_id,
            MessageRequest={
                'Addresses': {
                    destination_number: {
                        'ChannelType': 'VOICE'
                    }
                },
                'MessageConfiguration': {
                    'VoiceMessage': message['VoiceMessage']
                }
            }
        )