import requests, json, time, webhook, Database
import sqlite3

# Implement json config
servers = {"TestServer":"http://127.0.0.1:5000/webhook"}
server_stats = {"TestServer": None}
db = Database.RegistryDB("Registry.db")

while True:
    server_stats = webhook.fetch_server_data(servers)
    for x in server_stats:
        print(server_stats[x])
        db.write_data(x, server_stats[x])
    time.sleep(1)
