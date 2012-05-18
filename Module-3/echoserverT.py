#!/usr/bin/env python

import socket, threading, signal, sys

class WorkerThread(threading.Thread):

        def __init__(self, client):
                threading.Thread.__init__(self)
                self.client = client

        def run(self):
                data = "dummy"
                while len(data):
                        data = self.client.recv(2048)
                        print "Client sent: ", data
                        self.client.send(data)

                print "Closing connection ..."
                self.client.close()

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

        worker = WorkerThread(client)
        worker.setDaemon(True)
        worker.start()
