# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 22:38:26 2017

@author: impROS
"""

import socket
host = "localhost"
port = 8098
buf = 1024
calistir = (host,port)
istemci = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
istemci.connect(calistir)
veri = istemci.recv()
print(veri)
istemci.send("impROS ")
istemci.close()