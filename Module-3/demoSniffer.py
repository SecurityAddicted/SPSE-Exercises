#!/usr/bin/env python

import socket, struct, binascii

IP, TCP, HTTP = False, False, False

class bf(object):
    def __init__(self,value=0):
        self._d = value

    def __getitem__(self, index):
        return (self._d >> index) & 1

    def __setitem__(self,index,value):
        value    = (value&1L)<<index
        mask     = (1L)<<index
        self._d  = (self._d & ~mask) | value

    def __getslice__(self, start, end):
        mask = 2L**(end - start) -1
        return (self._d >> start) & mask

    def __setslice__(self, start, end, value):
        mask = 2L**(end - start) -1
        value = (value & mask) << start
        mask = mask << start
        self._d = (self._d & ~mask) | value
        return (self._d >> start) & mask

    def __int__(self):
        return self._d

def parseETH(header):
        eth_hdr = struct.unpack("!6s6s2s", header)
        global IP
        print "Source MAC address: ", binascii.hexlify(eth_hdr[0])
        print "Destination MAC address: ", binascii.hexlify(eth_hdr[1])
        if binascii.hexlify(eth_hdr[2]) == '0800':
                IP = True

def parseIP(header):
        ip_hdr = struct.unpack("!9s1s2s4s4s", header)
        global TCP
        print "Source IP address: ", socket.inet_ntoa(ip_hdr[3])

        print "Destination IP address: ", socket.inet_ntoa(ip_hdr[4])

        if binascii.hexlify(ip_hdr[1]) == '06':
                TCP = True

def parseTCP(header):
        tcp_orf = bf()
        global HTTP
        (tcp_sp, tcp_dp, tcp_sn, tcp_an, tcp_orf[0:16], tcp_w, tcp_ck, tcp_u) = struct.unpack("!HHLLHHHH", header)

        print "Source port number: ", tcp_sp
        print "Destination port number: ", tcp_dp
        print "Sequence number: ", tcp_sn
        print "Acknowlegement number: ", tcp_an
        print "Offset: ", int(tcp_orf[0:4])
        print "URG: ", tcp_orf[10]
        print "ACK: ", tcp_orf[11]
        print "PSH: ", tcp_orf[12]
        print "RST: ", tcp_orf[13]
        print "SYN: ", tcp_orf[14]
        print "FIN: ", tcp_orf[15]
        print "Window number: ", tcp_w
        print "Checksum: ", tcp_ck
        print "Urgent Pointer: ", tcp_u
        if (tcp_sp == 80 ) or (tcp_dp == 80):
                HTTP = True

def parseHTTP(data):
        print "HTTP data: ", data

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

while 1:
        pkt = rawSocket.recvfrom(2048)
        IP, TCP, HTTP = False, False, False
        parseETH(pkt[0][0:14])
        if IP:
                parseIP(pkt[0][14:34])
        if TCP:
                parseTCP(pkt[0][34:54])
        if HTTP:
                parseHTTP(pkt[0][54:])

        print "-----------------------"
