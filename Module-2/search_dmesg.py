#!/usr/bin/python

dmesg = open("/var/log/dmesg", "r")
for line in dmesg.readlines():
        if ("usb" or "USB") in line:
                print line,
dmesg.close()
