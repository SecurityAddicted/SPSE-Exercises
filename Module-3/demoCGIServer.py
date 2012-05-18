#!/usr/bin/env python

import SocketServer, CGIHTTPServer

class HttpRequestHandler(CGIHTTPServer.CGIHTTPRequestHandler):

        def do_GET(self):
                if self.path == "/admin":
                        self.wfile.write("This page is only for Admins!")
                        #self.wfile.write(self.headers)
                else:
                        CGIHTTPServer.CGIHTTPRequestHandler.do_GET(self)

httpServer = SocketServer.TCPServer(("0.0.0.0", 10000), HttpRequestHandler)
httpServer.server_name = 'localhost'
httpServer.server_port = 10000
httpServer.serve_forever()
