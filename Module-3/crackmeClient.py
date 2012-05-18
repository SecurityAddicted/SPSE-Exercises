#!/usr/bin/env python

import socket, sys

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.connect((sys.argv[1], 1337))
(ip, port) = tcpSocket.getsockname()

while 1:
        tcpSocket.send(str(port))
        result =  tcpSocket.recv(2048)
        print result
        if "Winner" in result:
                print "Cracked! Password is ", str(port)
                break

tcpSocket.close()
