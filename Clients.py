import socket
import threading

# Get user's name
name = input("Choose your name: ").strip()

# Ensure a name is provided
while not name:
    name = input("You should provide name: ").strip()

# Create a socket object
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server details
ADDRESS = "192.168.1.4"
PORT = 7000

# Connect to the server
socket_obj.connect((ADDRESS, PORT))

# Function to handle sending messages
def sending_msg():
    print("Enter your message: ")
    while True:
        sent_msg = input()
        # Get message from user
        
        # Check if message is not empty
        if sent_msg:
            # Concatenate name with the message
            msg_name = name + " : " + sent_msg
            
            # Send message to server
            socket_obj.send(msg_name.encode())

# Function to handle receiving messages
def recieve_msg():
    while True:
        # Receive message from server
        recieved_msg = socket_obj.recv(1024).decode()
        
        # Print received message
        print(recieved_msg)

# Create threads for sending and receiving messages
thread_send = threading.Thread(target=sending_msg)
thread_receive = threading.Thread(target=recieve_msg)

# Start threads
thread_send.start()
thread_receive.start()