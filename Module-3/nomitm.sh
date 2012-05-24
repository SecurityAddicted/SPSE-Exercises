#!/bin/sh

killall python ./arpSpoofer.py

echo 0 > /proc/sys/net/ipv4/ip_forward
