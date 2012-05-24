#!/usr/bin/env python

from scapy.all import *
import netifaces
import netaddr
import socket
from pprint import pformat

myiface = 'eth0'
addrs = netifaces.ifaddresses(myiface)

ipinfo = addrs[socket.AF_INET][0]
address = ipinfo['addr']
netmask = ipinfo['netmask']

cidr = netaddr.IPNetwork('%s/%s' % (address, netmask))

for ip in cidr:
        arpRequest = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=str(ip), hwdst="ff:ff:ff:ff:ff:ff")
        arpResponse = srp1(arpRequest, timeout=1, verbose=0)
        if arpResponse:
                print "IP: " + arpResponse.psrc + "    MAC: " + arpResponse.hwsrc
