import socket, signal

# Client setup
HOST = '127.0.0.1'  # Server address (localhost)
PORT = 65432        # Port to connect to

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))  # Connect to the server
        print("Connected to server!")
        
        while True:
            message = input("Enter message to send to the server (or 'exit' to quit): ")
            if message.lower() == 'exit':
                print("Exiting...")
                break
            
            s.sendall(message.encode())  # Send message to server
            data = s.recv(1024)  # Receive response from server
            print(f"Server response: {data.decode()}")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Make sure SIGINT is handled by Python
    start_client()