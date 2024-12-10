import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message.lower() == 'exit':
            print("Client has disconnected.")
            break
        print(f"Client: {message}")
        response = input("Server: ")
        client_socket.send(response.encode('utf-8'))
        if response.lower() == 'exit':
            break

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
