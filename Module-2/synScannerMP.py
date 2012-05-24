#!/usr/bin/env python

import multiprocessing, sys, getopt
from scapy.all import *

NUM_PROCESS = 5

def synScan(q):
        while not q.empty():
                (ip, port) = q.get()
                response = sr1(IP(dst=ip)/TCP(dport=port, flags="S"), timeout=1, verbose=0)
                if response:
                        if response.sprintf("%TCP.flags%") == "SA":
                                print "Port " + str(port) + " open"
                else:
                        print "Port " + str(port) + " closed"
        return

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
        queue = multiprocessing.Queue()
        if args[1].find(",") > 0:
                ports = args[1].split(",")
                for port in ports:
                        if port.find("-") > 0:
                                subports = port.split("-")
                                for subport in range(int(subports[0]), int(subports[1])+1):
                                        queue.put((args[0], subport))
                        else:
                                queue.put((args[0], int(port)))
        elif args[1].find("-") > 0:
                ports = args[1].split("-")
                for port in range(int(ports[0]), int(ports[1])+1):
                        queue.put((args[0], port))
        else:
                queue.put((args[0], int(args[1])))
        global NUM_PROCESS
        jobs = []
        for i in range(NUM_PROCESS):
                worker = multiprocessing.Process(target=synScan, args=(queue,))
                worker.daemon = True
                jobs.append(worker)
                worker.start()
        queue.close()
        queue.join_thread()
        for j in jobs:
                j.join()

if __name__ == "__main__":
    main(sys.argv[1:])
