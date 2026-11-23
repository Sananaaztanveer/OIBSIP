
# Python Chat Application

## About the Project
This is a beginner-level real-time chat application built using Python.
It allows two or more clients to communicate with each other through a server using localhost.

## Technologies Used
- Python
- Socket Programming
- Threading
- DateTime

## Project Files
- server.py – Handles client connections and message sharing.
- client.py – Allows users to send and receive messages.

## Features
1. Server listens for incoming client connections.
2. Clients connect to the server.
3. Real-time, bidirectional messaging.
4. Messages display timestamps.
5. Disconnection notifications.
6. Runs locally using localhost.

## How to Run

### Step 1: Start the Server
Open Command Prompt and run:

```bash
py server.py
```

### Step 2: Start the Client
Open another Command Prompt and run:

```bash
py client.py
```

Enter your username and start chatting.

To leave the chat, type `exit`.

## How Messages Are Handled
Messages are sent between clients through the server using Python sockets.
The server forwards messages to the other connected clients.

## Security Note
This beginner project does not encrypt messages. Messages are transmitted as plain text and should not be used for private or sensitive communication.

## Author
Sananaaz Tanveer
