from multiprocessing import Process
import os
from time import sleep

def worker(x):
    #sleep(2)
    print(f'hello {x}')
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

if __name__ == '__main__':
      print('module name:', __name__)
      process = Process(target=worker, args=("python",))
      print(process)
      process.start()
      process.join()

