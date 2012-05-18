#!/usr/bin/env python

import SocketServer, SimpleHTTPServer

class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

        def do_GET(self):
                if self.path == "/admin":
                        self.wfile.write("This page is only for Admins!")
                        #self.wfile.write(self.headers)
                else:
                        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpServer = SocketServer.TCPServer(("0.0.0.0", 10000), HttpRequestHandler)

httpServer.serve_forever()
