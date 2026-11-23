
import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Enter your name: ")

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print("\n" + message)

        except:
            print("\nDisconnected from server.")
            break

thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()

print("Connected to chat!")
print("Type 'exit' to leave.")

while True:
    message = input()

    if message.lower() == "exit":
        break

    client.send(f"{username}: {message}".encode())

client.close()
