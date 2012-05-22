#!/usr/bin/env python

from scapy.all import *

interface = "wlan0"

bssidList = []

def sniffSsid(pkt):
        global bssidList
        if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
                if pkt.addr3 not in bssidList:
                        print pkt.sprintf("%Dot11.addr3%\t%Dot11Beacon.info%\t%Dot11Beacon.cap%")
                        bssidList.append(pkt.addr3)
        elif pkt.haslayer(Dot11ProbeResp):
                if pkt.addr3 not in bssidList:
                        print pkt.sprintf("%Dot11.addr3%\t%Dot11ProbeResp.info%\t%Dot11ProbeResp.cap%")
                        bssidList.append(pkt.addr3)


sniff(iface=interface, prn=sniffSsid)
