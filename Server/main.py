import requests, json, time, webhook

# Implement json config
servers = {"TestServer1":"http://127.0.0.1:5000/webhook"}
server_stats = {"TestServer1": None}

while True:
    server_stats = webhook.fetch_server_data(servers)
    for x in server_stats:
        print(x, server_stats[x])
    time.sleep(1)