#!/usr/bin/env python

from scapy.all import *

def printHttpData(pkt):
        httpLoad = pkt.sprintf("%Raw.load%")
        print pkt.summary()
        #print httpLoad
        if httpLoad.startswith("'GET") or httpLoad.startswith("'POST"):
                httpData = httpLoad[1:-1].split("\\r\\n")
                a = httpData[0].split()
                print "GET/POST data: ", a[1]
                del httpData[0]
                for item in httpData:
                        print item
        elif httpLoad.startswith("'HTTP"):
                httpData = httpLoad[1:-1].split("\\r\\n")
                del httpData[0]
                for item in httpData:
                        print item
        print "---------------------------------------------------------"

sniff(filter="tcp port 80", prn=printHttpData, store=0)
