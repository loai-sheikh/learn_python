import time

#low-level, old & deprecated 'thread' for module backwards incompatibilities in Python3
#threading module provides an easier to use and higher-level threading API built on top of this module
from _thread import start_new_thread, allocate_lock

##the lock idea

lock = allocate_lock()
sumOfNumbers = 0

def calculateSum(n):
      global sumOfNumbers
      for i in range(n):
            #close lock
            lock.acquire()
            sumOfNumbers += 1
            #open lock
            lock.release()


###Start The threads
start_new_thread(calculateSum, (1000000//2,))
start_new_thread(calculateSum, (1000000//2,))

#give time for calculations...
time.sleep(3)

#working, but this is really evil
print(sumOfNumbers)