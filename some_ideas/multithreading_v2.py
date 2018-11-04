# многопоточность
# -*- coding: utf-8 -*-
#import random
import time
from threading import Thread

class TestThread(Thread):
    def __init__(self, data):
        Thread.__init__(self)
        self._value = data
        
    def run(self):
        wait_time = 7
        print("Run TestThread1. value={}.  Wait for {} sec ".format(self._value, wait_time))
        time.sleep(wait_time)
        print("End of TestThread1.run")


class ForThread(Thread):
    def __init__(self, number):
        Thread.__init__(self)
        self._number = number

    def run(self):
        print("ForThread.run begin")
        for n in range(self._number):
            print("n={}".format(n))
            time.sleep(1)
        print("ForThread,run end")        

thread1 = TestThread(123)
thread1.start()

thread2 = ForThread(10)
thread2.start()

print("Main. Before join")
thread1.join()
print("Main. After join")
time.sleep(2)

print("Finish main thread")
