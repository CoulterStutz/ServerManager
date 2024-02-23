import requests, json, time, webhook
import sqlite3, AWS
import config

servers = config.QuerySettings["QueryServers"]
server_stats = {"TestServer": None}

cw = AWS.CloudWatch("us-west-1")

while True:
    server_stats = webhook.fetch_server_data(servers)
    for x in server_stats:
        print(server_stats[x])
        cw.report_metric(x, server_stats[x], minimal=config.QuerySettings["minimalistMode"])
    time.sleep(config.QuerySettings["FetchAndReportDelay"])
