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
    def __init__(self, number, value):
        Thread.__init__(self)
        self._number = number
        self._value = value

    def run(self):
        print("ForThread.run begin")
        for n in range(self._number):
            print("n={} value={}".format(n, self._value))
            time.sleep(1)
        print("ForThread,run end")        

    def set_value(self, value):
        self._value = value
        

thread1 = TestThread(123)
thread1.start()

thread2 = ForThread(10,100)
thread2.start()



for n in range(3):    
    time.sleep(2)
    thread2.set_value(200+n)


thread2.join()

print("Main. Before join")
thread1.join()
print("Main. After join")


print("Finish main thread")
