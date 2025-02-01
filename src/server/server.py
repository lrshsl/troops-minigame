import socket, signal

# Server setup
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on (non-privileged ports > 1023)

def send_troops(rest: str):
    t1, t2 = rest[:2]
    print(f"Sending troops from {t1} to {t2}")

commands = {
    'send': send_troops,
}

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server started, waiting for a connection on {HOST}:{PORT}")
        
        conn, addr = s.accept()  # Accept a new connection
        with conn:
            print(f"Connected by {addr}")
            while data := conn.recv(128).decode():
                print(f"Received: {data}")
                
                cmd, rest = data[:4], data[5:]
                commands[cmd](rest)
                
                conn.sendall(data.encode())  # Echo the message back to the client

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Make sure SIGINT is handled by Python
    start_server()