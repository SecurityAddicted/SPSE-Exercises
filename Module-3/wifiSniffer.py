#!/usr/bin/env python

from scapy.all import *
import sys, getopt, netifaces

bssidList = []

def usage():
        print "Usage: sudo ./wifiSniffer.py <interface>"

def sniffSsid(pkt):
        global bssidList
        if pkt.haslayer(Dot11Beacon):
                if pkt.addr2 not in bssidList:
                        print pkt.sprintf("%Dot11.addr2%\t%Dot11Beacon.info%\t%Dot11Beacon.cap%")
                        bssidList.append(pkt.addr3)
        elif pkt.haslayer(Dot11ProbeResp):
                if pkt.addr2 not in bssidList:
                        print pkt.sprintf("%Dot11.addr2%\t%Dot11ProbeResp.info%\t%Dot11ProbeResp.cap%")
                        bssidList.append(pkt.addr3)
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
        if (len(args) > 0) and (args[0] in netifaces.interfaces()):
                sniff(iface=args[0], prn=sniffSsid, store=0)
        else:
                print "Interface not specified or wrong"

if __name__ == "__main__":
        main(sys.argv[1:])
