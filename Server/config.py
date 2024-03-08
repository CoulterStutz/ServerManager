QuerySettings = {
    "FetchAndReportDelay": 5,
    "minimalistMode": False,
    "QueryServers": {
        "TestServer": "http://127.0.0.1:5001/webhook"
    }
}

AWSSettings = {
    "RegionName": "us-west-2",
    "CloudWatchSettings": {
      "MetricReporting": True
    },
    "PinpointSettings": {
        "ApplicationID": "YOUR-APPLICATION-ID",
        "DestinationNumbers": [],
        "AlertIgnoreList": "TestServer",
        "AlertSettings": {
            "CallWhenServersDown": True,
            "CustomServerMetrics": {
                "TotalCPUUsage": {
                    "ValueGreaterThen": 90,
                    "ValueLessThen": 3
                }
            }
        }
    }
}

InterfaceSettings = {
    "IP": "0.0.0.0",
    "Port": 80,
    "PasswordAuthentication": False,
    "Metrics": {
        "AWSCPUMetricsLink": "",
        "AWSStorageMetricsLink": "",
        "AWSNetworkMetricsLink": "",
        "AWSRamMetricsLink": "",
        "CustomMetrics": {}
    }
}
