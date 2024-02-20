import requests

def fetch_server_data(servers):
    server_stats = {}
    for x in servers:
        server_stats[x] = None

    for x in servers:
        response = requests.get(servers[x])

        if response.status_code == 200:
            data = response.json()
            server_stats[x] = data
        else:
            print("Failed to fetch data from webhook")

    return server_stats