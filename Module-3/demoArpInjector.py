#!/usr/bin/env python

import socket, struct

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

rawSocket.bind(("eth0", socket.htons(0x0800)))

packet = struct.pack("!6s6s2s2s2s1s1s2s6s4s6s4s",
"\xff\xff\xff\xff\xff\xff", "\xab\xab\xab\xab\xab\xab", "\x08\x06", "\x00\x01",
"\x08\x00", "\x06", "\x04", "\x00\x01", "\xab\xab\xab\xab\xab\xab", "\xff\xff\xff\xff",
"\x00\x00\x00\x00\x00\x00", "\xff\xff\xff\xff")

rawSocket.send(packet)
