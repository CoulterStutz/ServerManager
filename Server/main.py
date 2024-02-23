import requests, json, time, webhook
import sqlite3, AWS

# Implement json config
servers = {"TestServer":"http://127.0.0.1:5000/webhook"}
server_stats = {"TestServer": None}

cw = AWS.CloudWatch("us-west-2")

while True:
    server_stats = webhook.fetch_server_data(servers)
    for x in server_stats:
        print(server_stats[x])
        cw.report_metric(x, server_stats[x])
    time.sleep(1)
