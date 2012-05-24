#!/usr/bin/env python

from scapy.all import *
from netaddr import valid_ipv4
import sys, getopt

def usage():
        print "Usage: sudo ./dnsFuzzer.py [-i interface] [-l] [target ip]"
        print "Options:   -l     loop sending"

def main(argv):
        loopSend = 0
        try:
                opts, args = getopt.getopt(argv, "hi:l")
        except getopt.GetoptError:
                usage()
                sys.exit(2)
        for opt, arg in opts:
                if opt in ("-h"):
                        usage()
                        sys.exit()
                elif opt in ("-i"):
                        conf.iface = arg
                elif opt in ("-l"):
                        loopSend = 1
        if len(args) > 0:
                if not valid_ipv4(args[0], flags=1):
                        print "Target IP not valid"
                        sys.exit(2)
                a = fuzz(IP(dst=args[0])/UDP(dport=53)/DNS(qd=fuzz(DNSQR()), an=fuzz(DNSRR())))
                send(a, loop=loopSend)
        else:
                a = fuzz(IP()/UDP(dport=53)/DNS(qd=fuzz(DNSQR()), an=fuzz(DNSRR())))
                send(a, loop=loopSend)

if __name__ == "__main__":
        main(sys.argv[1:])
