#!/usr/bin/env python

import SocketServer, SimpleHTTPServer, signal, sys, getopt

httpServer = 0

class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

        def do_GET(self):
                if self.path == "/admin":
                        self.wfile.write("This page is only for Admins!")
                        #self.wfile.write(self.headers)
                else:
                        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

def receivedAlarm(signum, frm):
        global httpServer
        #httpServer.shutdown()     #don't work correctly, block the program
        sys.exit(0)

def main(argv):
        signal.signal(signal.SIGALRM, receivedAlarm)
        try:
                opts, args = getopt.getopt(argv, "hs:")
        except getopt.GetoptError:
                usage()
                sys.exit(2)
        for opt, arg in opts:
                if opt in ("-h"):
                        usage()
                        sys.exit()
                elif opt in ("-s"):
                        signal.alarm(int(arg))
        global httpServer
        httpServer = SocketServer.TCPServer(("0.0.0.0", 10000), HttpRequestHandler)
        httpServer.allow_reuse_address = True
        httpServer.serve_forever()

if __name__=="__main__":
        main(sys.argv[1:])
