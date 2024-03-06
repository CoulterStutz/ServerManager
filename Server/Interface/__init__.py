import socket
import threading
import sys
from sql import *

class SocketServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.auth_db = AuthDB()
        self.permissions_db = PermissionsDB()

    def listen_for_client(self, client):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message:
                    print(f"Received command from client: {message}")
                    # Handle command here
            except Exception as e:
                print(f"Error handling client message: {e}")
                client.close()
                break

    def start(self):
        self.server.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client, address = self.server.accept()
            print(f"Connection from {address} has been established.")

            # Authenticate user
            username = client.recv(1024).decode('utf-8')
            password = client.recv(1024).decode('utf-8')
            if self.auth_db.check_auth(username, password):
                print("User authenticated successfully.")
                client.send("Authentication successful.".encode('utf-8'))
                threading.Thread(target=self.listen_for_client, args=(client,)).start()
            else:
                print("Authentication failed.")
                client.send("Authentication failed.".encode('utf-8'))
                client.close()

    def accept_commands(self):
        while True:
            try:
                command = input("\nServerManager>> ")
                if command.split()[0] == "add":
                    if command.split()[1] == "new-authed-user":
                        auth_info = command.split()[2], command.split()[3], command.split()[4]
                        print(auth_info)
                if command == "exit":
                    self.server.close()
                    sys.exit()
            except IndexError:
                None

if __name__ == "__main__":
    server = SocketServer('localhost', 12345)
    threading.Thread(target=server.start).start()
    server.accept_commands()
