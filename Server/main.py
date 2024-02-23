import requests, json, time, webhook
import sqlite3, AWS
import config

servers = config.QuerySettings["QueryServers"]
server_stats = {}

cw = AWS.CloudWatch(config.AWSSettings["RegionName"])
p = AWS.PinPoint('us-west-2', config.AWSSettings["PinpointSettings"]["ApplicationID"], config.AWSSettings["PinpointSettings"]["DestinationNumbers"])

dead_servers = []

while True:
    dead_server = []
    server_stats = webhook.fetch_server_data(servers)
    for x in server_stats:
        if server_stats[x] != 0:
            print(server_stats[x])
            cw.report_metric(x, server_stats[x], minimal=config.QuerySettings["minimalistMode"])
        else:
            if x not in dead_servers:
                dead_server.append(x)
            else:
                continue

    for x in dead_server:
        p.send_death_message(dead_server)
        print(f'server go fuck, amazon know now :P {dead_server}')
        dead_servers.append(x)

    time.sleep(config.QuerySettings["FetchAndReportDelay"])
