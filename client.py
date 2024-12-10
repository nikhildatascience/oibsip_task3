import socket
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    client_socket.connect((host, port))
    print("Connected to the server!")
    while True:
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            print("Exiting the chat...")
            break
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server: {response}")
        if response.lower() == 'exit':
            print("Server has disconnected.")
            break
    client_socket.close()

if __name__ == "__main__":
    start_client()
