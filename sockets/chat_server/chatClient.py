#client code:
import socket
import threading

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.105", 4434)) #enter server address & port number

def job():
      while True:
            s.send(input().encode())

t = threading.Thread(target=job)
t.start()

while True:
      try: 
            print(s.recv(1024).decode())
      except:
            pass