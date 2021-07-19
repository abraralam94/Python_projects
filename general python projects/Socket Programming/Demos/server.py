import socket
import threading

PORT = 5050
#SERVER = "192.168.0.49"
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
