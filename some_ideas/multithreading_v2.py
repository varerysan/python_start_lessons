# многопоточность
# -*- coding: utf-8 -*-
#import random
import time
from threading import Thread


#class MyThread(Thread):
#    """
#    A threading example
#    """
#    
#    def __init__(self, name):
#        """Инициализация потока"""
#        Thread.__init__(self)
#        self.name = name
#    
#    def run(self):
#        """Запуск потока"""
#        amount = random.randint(3, 15)
#        time.sleep(amount)
#        msg = "%s is running" % self.name
#        print(msg)


class TestThread(Thread):
    def __init__(self, data):
        Thread.__init__(self)
        self._value = data
        
    def run(self):
        wait_time = 2
        print("Run TestThread1. value={}.  Wait for {} sec ".format(self._value, wait_time))
        time.sleep(wait_time)
        print("End of TestThread1.run")
        

thread1 = TestThread(123)
thread1.start()

print("Main. Before join")
print("Finish main thread")
