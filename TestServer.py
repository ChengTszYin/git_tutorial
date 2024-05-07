import socket
import threading

HEADER = 64
DISCONNECT_MSG = "!DISCONNTECT"
PORT = 7001
SERVER = socket.gethostbyname(socket.gethostname()) #SERVER = "192.168.1.104"
Addr = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(Addr)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode('utf-8')
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode('utf-8')
        if msg == DISCONNECT_MSG:
            connected = False
        print(f'[{addr}] {msg}')
    conn.close()
    
def start():
    server.listen()
    print(f'LISTENING on {server}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.activeCount() - 1}")

print("[STARTING NOW]")
start()


