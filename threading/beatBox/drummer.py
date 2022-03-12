import csv
import time
import threading
import os
import sys
from playsound import playsound

folder_path = os.path.join(sys.path[0])
def runSound(name):    
    playsound(folder_path+f"\samples\{name}.wav")

while True:
      with open(folder_path+'\sequenser.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                  print(row)
                  for step in row:
                        print(step+"\t", end="")
                        s_thread = threading.Thread(target=runSound, args=(), kwargs={"name":step})
                        s_thread.start()
                        time.sleep(0.1)
                  print()
      print("next loop...")