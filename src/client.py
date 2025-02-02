import socket, signal
from typing import Callable

# Client setup
HOST = '127.0.0.1'  # Server address (localhost)
PORT = 65432        # Port to connect to

def start_client(main_loop):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Connected to server!")
        
        main_loop(s)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Make sure SIGINT is handled by Python
    start_client()
