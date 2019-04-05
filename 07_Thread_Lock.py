# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 12:24:39 2018

@author: impROS
"""

import threading

print("Press Escape to Quit")

# Global variable
data = None

class threadOne(threading.Thread):
    def run(self):
        self.setup()

    def setup(self):
        global data
        print ('hello world - this is threadOne')

        with lock:
            print ("Thread one has lock")
            data =5


class threadTwo(threading.Thread):
    def run(self):
        global data
        print('ran')
        print ("Waiting")

        with lock:
            print("Thread two has lock")
            print(data)

lock = threading.Lock()

threadOne().start()
threadTwo().start()