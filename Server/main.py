import threading
import time, webhook
import config, AWS
from termcolor import colored

servers = config.QuerySettings["QueryServers"]
server_stats = {}

cw = AWS.CloudWatch(config.AWSSettings["RegionName"])
p = AWS.PinPoint('us-west-2', config.AWSSettings["PinpointSettings"]["ApplicationID"], config.AWSSettings["PinpointSettings"]["DestinationNumbers"])
custom_metrics = config.AWSSettings["PinpointSettings"]["AlertSettings"]["CustomServerMetrics"]

dead_servers = []

def query_loop():
    while True:
        dead_server = []
        server_stats = webhook.fetch_server_data(servers)
        for x in server_stats:
            if server_stats[x] != 0:
                print(f"{colored('Recieved Data', 'magenta')}: {x}")
                if config.AWSSettings["CloudWatchSettings"]["MetricReporting"]:
                    cw.report_metric(x, server_stats[x], minimal=config.QuerySettings["minimalistMode"])
            else:
                if x not in dead_servers:
                    dead_server.append(x)
                    print(f'{colored("DEAD SERVERS FOUND: ")}: {dead_server}')
                else:
                    print(f'{colored("DEAD SERVER CAUSING TRAFFIC!", "red")}: {dead_servers}')
                    continue

        for x in dead_server:
            if config.AWSSettings["PinpointSettings"]["AlertSettings"]["CallWhenServersDown"] and x not in config.AWSSettings["PinpointSettings"]["AlertIgnoreList"]:
                p.send_death_message(dead_server)
                print(f'{colored("Call Initiated")}: For Dead Servers {dead_server}')
            dead_servers.append(x)

        time.sleep(config.QuerySettings["FetchAndReportDelay"])


if __name__ == "__main__":
    wh_thread = threading.Thread(target=query_loop())
    wh_thread.start()