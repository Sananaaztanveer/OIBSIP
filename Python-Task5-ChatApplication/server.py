
import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 12345

clients = []

def handle_client(client_socket, address):
    print(f"Connected: {address}")

    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                break

            timestamp = datetime.now().strftime("%H:%M")
            formatted_message = f"[{timestamp}] {message}"

            print(formatted_message)

            for client in clients:
                if client != client_socket:
                    client.send(formatted_message.encode())

        except:
            break

    if client_socket in clients:
        clients.remove(client_socket)

    client_socket.close()
    print(f"Client disconnected: {address}")

    for client in clients:
        try:
            client.send("A user has disconnected.".encode())
        except:
            pass


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Chat server is running...")
print("Waiting for clients...")

while True:
    client_socket, address = server.accept()
    clients.append(client_socket)

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, address)
    )
    thread.start()
