import requests, json, time, webhook

# Implement json config
servers = {"TestServer1":"http://127.0.0.1:5000/webhook"}
server_stats = {"TestServer1": None}

while True:
    server_stats = webhook.fetch_server_data(servers)
    print(server_stats)
    time.sleep(1)