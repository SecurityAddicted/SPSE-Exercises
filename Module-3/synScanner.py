#!/usr/bin/env python

from scapy.all import *
import sys, getopt

def usage():
        print "Usage: sudo ./synScanner.py <host> <port>"

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
        response = sr1(IP(dst=args[0])/TCP(dport=int(args[1]), flags="S"), timeout=5, verbose=0)
        if response:
                if response.sprintf("%TCP.flags%") == "SA":
                        print "Port " + args[1] + " open"
                else:
                        print "Port " + args[1] + " closed"
        else:
                print "No response"

if __name__ == "__main__":
    main(sys.argv[1:])

