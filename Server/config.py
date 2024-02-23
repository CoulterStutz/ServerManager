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
        "ApplicationID": "YOUR-APPLICATION-ID",
        "DestinationNumbers": [],
        "AlertSettings": {
            "CallWhenServerDown": True,
        }
    }
}
