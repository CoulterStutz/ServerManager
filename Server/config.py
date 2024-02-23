QuerySettings = {
    "FetchAndReportDelay": 5,
    "minimalistMode": False,
    "QueryServers": {
        "TestServer": "http://127.0.0.1:5001/webhook"
    }
}

AWSSettings = {
    "RegionName": "us-west-2",
    "PinpointSettings": {
        "ApplicationID": "3441d6e35f524c6ea2f1f3f6512fa97b",
        "DestinationNumbers": ["+17202020350"],
        "AlertSettings": {
            "CallWhenServerDown": True,
        }
    }
}