import socket

c = socket.socket()
c.connect(("192.168.0.105", 1234))

while True:
    print(c.recv(126).decode())