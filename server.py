import socket, signal, json

from src.levels import towers
from src.constants import *

# Server setup
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on (non-privileged ports > 1023)

def send_troops(conn, rest: str):
    n, t1, t2 = rest.split(maxsplit=2)
    print(f"Sending {n} troops from {t1} to {t2}")

def init_game(conn, rest: str):
    conn.sendall(json.dumps(state))

reset_game = init_game

commands = {
    'init': init_game,
    'send': send_troops,
    'rset': reset_game,
}

company = lambda name, color: {
    name: {
        'color': color,
        'towers': [t for t in towers if t.color == color],
    }
}
state = {
    'companies': [
        company('player 1', p1_color),
        company('player 2', p2_color),
        company('neutral', n_color),
    ],
}

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server started, waiting for a connection on {HOST}:{PORT}")
        
        while True:
            conn, addr = s.accept()  # Accept a new connection

            with conn:
                print(f"Connected by {addr}")


                while data := conn.recv(128).decode():
                    print(f"Received: {data}")
                    
                    cmd, rest = data[:4], data[5:]
                    commands[cmd](conn, rest)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Make sure SIGINT is handled by Python
    start_server()

