#!/usr/bin/env python

import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpSocket.bind(("0.0.0.0", 8000))
tcpSocket.listen(2)

print "Waiting for a client ... "
(client, (ip, port)) = tcpSocket.accept()

print "Received connection from: ", ip, port
print "Starting ECHO output ... "

data = "dummy"

while len(data):
        data = client.recv(2048)
        print "Client sent: ", data
        client.send(data)

print "Closing connection ..."
client.close()

print "Shutting down server ..."
tcpSocket.close()
