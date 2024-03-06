import socket, threading, sqlite3

class InterfaceServer():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.client_threads = []

    def start(self):
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            client_socket, address = self.server_socket.accept()
            print(f"Connected to {address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, address))
            client_thread.start()
            self.client_threads.append(client_thread)

    def handle_client(self, client_socket, address):
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received data from {address}: {data.decode()}")
                client_socket.sendall(data)  # Echo back the data
            except Exception as e:
                print(f"Error handling client {address}: {e}")
                break
        print(f"Closing connection to {address}")
        client_socket.close()

    def stop(self):
        print("Stopping server...")
        for client_thread in self.client_threads:
            client_thread.join()
        self.server_socket.close()