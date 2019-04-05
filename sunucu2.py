# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 00:21:31 2017

@author: impROS
"""

import socket
 
def Main():
        host = 'localhost' 
        port = 8098
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        message = "impROS"
         
        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                 
                print ('Received from server: ' + data)
                 
              
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()