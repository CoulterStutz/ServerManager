import requests, json, time, webhook
import sqlite3, AWS
import config

servers = config.QuerySettings["QueryServers"]
server_stats = {}

cw = AWS.CloudWatch(config.AWSSettings["RegionName"])
p = AWS.PinPoint('us-west-2', config.AWSSettings["PinpointSettings"]["ApplicationID"], config.AWSSettings["PinpointSettings"]["DestinationNumbers"])

while True:
    server_stats = webhook.fetch_server_data(servers)
    for x in server_stats:
        print(server_stats[x])
        cw.report_metric(x, server_stats[x], minimal=config.QuerySettings["minimalistMode"])
    time.sleep(config.QuerySettings["FetchAndReportDelay"])
