import socket

HEADER = 64
PORT = 7001
#IP = socket.gethostbyname(socket.gethostname())
IP = "192.168.1.104"
ADDR = (IP,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode('utf-8')
    msg_length = len(message)
    send_length = str(msg_length).encode('utf-8')
    send_length += b' ' * (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)

send("Hello Asshole!")
    