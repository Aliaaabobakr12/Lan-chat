import socket
import threading


def initialize_server(address, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((address, port))
    server_socket.listen()
    print(f"Server listening on {address}:{port}")
    clients_list = []
    accept_clients(server_socket, clients_list)


def accept_clients(server_socket, clients_list):
    while True:
        client, client_address = server_socket.accept()
        clients_list.append(client)
        client_thread(client, clients_list)


def client_thread(client, clients_list):
    client_threading = threading.Thread(target=thread_listening, args=(client, clients_list))
    client_threading.start()


def thread_listening(client, clients_list):
    while True:
        message = client.recv(1024).decode()
        if message:
            print(f"Message from {client.getpeername()}: {message}")
            broadcast(message, clients_list)
        else:
            print(f"Client {client.getpeername()} disconnected")
            clients_list.remove(client)
            client.close()
        

def broadcast(message, clients_list):
    for client in clients_list:
        try:
            client.send(message.encode())
        except Exception as e:
            print(f"Error broadcasting message to {client.getpeername()}: {e}")
            clients_list.remove(client)
            client.close()


def main():
    my_port = 7000
    my_address = "192.168.1.4"
    initialize_server(my_address, my_port)


if __name__ == "__main__":
    main()
