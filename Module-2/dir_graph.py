#!/usr/bin/env python

import os, sys, time

def print_graph(dir, level):
        for item in os.listdir(dir):
                print_level(level)
                abs_item = os.path.join(os.path.abspath(dir),item)
                item_stat = os.stat(abs_item)
                print item, item_stat.st_size, time.ctime(item_stat.st_ctime)
                if os.path.isdir(abs_item):
                        print_graph(abs_item,level + 4)
        return

def print_level(level):
        for i in range(level):
                sys.stdout.write("-")
        return

start_dir = raw_input("Insert the start directory: ")
try:
        print_graph(os.path.abspath(start_dir), 0)
except Exception as e:
        print e
