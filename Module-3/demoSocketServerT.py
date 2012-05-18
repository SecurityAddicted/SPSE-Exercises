#!/usr/bin/env python

import SocketServer, threading

class ThreadedEchoHandler(SocketServer.BaseRequestHandler):

        def handle(self):
                print "Got Connection from ", self.client_address
                data = "dummy"
                while len(data):
                        data = self.request.recv(1024)
                        print "Client sent: ", data
                        self.request.send(data)
                print "Client left"

class ThreadedEchoServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
        pass

serverAddr = ("0.0.0.0", 9000)

server = ThreadedEchoServer(serverAddr, ThreadedEchoHandler)

t = threading.Thread(target=server.serve_forever())
t.setDaemon(True)
t.start()
