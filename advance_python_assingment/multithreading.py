# Exercise: Multithreading
# Create any multithreaded code using for loop for creating multithreads
# for i in range(10):
#     th = Thread(target=func_name, args=(i, ))
    
# print total active threads in multithreaded code using threading.active_count()

import time
import threading
from threading import Thread

def sleepMe(i):
    print("Thread %i will sleep." % i)
    time.sleep(5)
    print("Thread %i is awake" % i)

for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()
    print("Current Threads: %i." % threading.active_count())