#!/usr/bin/env python

import threading, Queue, sys, getopt
from scapy.all import *

NUM_THREAD = 5

def synScan(q):
        while not q.empty():
                (ip, port) = q.get()
                response = sr1(IP(dst=ip)/TCP(dport=port, flags="S"), timeout=1, verbose=0)
                if response:
                        if response.sprintf("%TCP.flags%") == "SA":
                                print "Port " + str(port) + " open"
                else:
                        print "Port " + str(port) + " closed"
                q.task_done()

def usage():
        print "Usage: sudo ./synScannerT.py <host> <port>"

def main(argv):
        try:
                opts, args = getopt.getopt(argv, "h")
        except getopt.GetoptError:
                usage()
                sys.exit(2)
        for opt, arg in opts:
                if opt in ("-h"):
                        usage()
                        sys.exit()
        if len(args) < 2:
                usage()
                sys.exit(2)
        queue = Queue.Queue()
        if args[1].find(",") > 0:
                ports = args[1].split(",")
                for port in ports:
                        if port.find("-") > 0:
                                subports = port.split("-")
                                for subport in range(int(subports[0]), int(subports[1])+1):
                                        queue.put((args[0], subport))
                                        print "Loading port: ", str(subport)
                        else:
                                queue.put((args[0], int(port)))
                                print "Loading port: ", str(port)
        elif args[1].find("-") > 0:
                ports = args[1].split("-")
                for port in range(int(ports[0]), int(ports[1])+1):
                        queue.put((args[0], port))
                        print "Loading port: ", str(port)
        else:
                queue.put((args[0], int(args[1])))
                print "Loading port: ", args[1]
        global NUM_THREAD
        for i in range(NUM_THREAD):
                worker = threading.Thread(target=synScan, args=(queue,))
                worker.setDaemon(True)
                worker.start()
        queue.join()

if __name__ == "__main__":
    main(sys.argv[1:])
