import socket

def start_client():
    # 1. Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Define the server's IP address and port
    host = '127.0.0.1'  # Must match the server's IP
    port = 65432        # Must match the server's port

    try:
        # 3. Connect to the server
        client_socket.connect((host, port))
        
        # 4. Send a message to the server
        message = "Hello, Server! This is the Python client."
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent: {message}")

        # 5. Receive the server's response
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")
        
    except ConnectionRefusedError:
        print("Connection failed. Is the server running?")
    finally:
        # 6. Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_client()
