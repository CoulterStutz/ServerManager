QuerySettings = {
    "FetchAndReportDelay": 60,
    "minimalistMode": False,
    "QueryServers": {
        "TestServer": "http://127.0.0.1:5000/webhook"
    }
}

AWSSettings = {
    "RegionName": "us-west-1",
    "PinpointSettings": {
        "AlertSettings": {
            "CallWhenServerDown": True,
        }
    }
}