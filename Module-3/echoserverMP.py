#!/usr/bin/env python

import socket, multiprocessing, signal, sys

def worker(client):
        data = "dummy"
        while len(data):
                data = client.recv(2048)
                print "Client sent: ", data
                client.send(data)

        print "Closing connection ..."
        client.close()

def ctrlcHandler(signum, frm):
        print "Shutting down server ..."
        tcpSocket.close()
        sys.exit(0)

signal.signal(signal.SIGINT, ctrlcHandler)
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpSocket.bind(("0.0.0.0", 8000))
tcpSocket.listen(5)

while True:
        print "Waiting for a client ... "
        (client, (ip, port)) = tcpSocket.accept()

        print "Received connection from: ", ip, port
        print "Starting ECHO output to: ", ip, port

        p = multiprocessing.Process(target=worker, args=(client,))
        p.start()
