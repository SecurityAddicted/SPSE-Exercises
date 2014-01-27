#!/usr/bin/env python

import signal

def ctrlc_handler(signum, frm):
        print "HAHA! You cannot kill me!"

print "Installing signal handler..............."

signal.signal(signal.SIGINT, ctrlc_handler)

print "Done!"

while True:
        pass
