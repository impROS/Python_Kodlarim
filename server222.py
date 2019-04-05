# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 22:34:59 2017

@author: impROS
"""

import socket
host = "127.0.0.1"
port = 8098
buf = 1024
calistir = (host,port)
print("basla")
bagla = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
bagla.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("basla")
bagla.bind(calistir)
bagla.listen(2)
sunucu,adres = bagla.accept()
print("basla")
sunucu.send("Baglanti Basarili..")
veri = sunucu.recv(buf)
print(veri)
sunucu.close()
bagla.close()