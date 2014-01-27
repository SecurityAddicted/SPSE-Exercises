#!/usr/bin/env python

dmesg = open("/var/log/messages", "r")
for line in dmesg.readlines():
        if ("usb" or "USB") in line:
                print line,
dmesg.close()
