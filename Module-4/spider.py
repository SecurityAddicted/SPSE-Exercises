#!/usr/bin/env python

import MySQLdb as mdb
import sys
from warnings import filterwarnings
import argparse
import mechanize


def create_db():
    try:
        conn = mdb.connect(host="localhost", user="root")
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    cur = conn.cursor()
    try:
        cur.execute("CREATE DATABASE IF NOT EXISTS myspider")
        cur.execute("USE myspider")
        cur.execute("""CREATE TABLE IF NOT EXISTS scan (
                        start INT NOT NULL)""")
#        conn.rollback()
    except mdb.Error as e:
        print "Error %d: %s" % (e.args[0], e.args[1])
#    conn.close()

def main():
    filterwarnings('ignore', category=mdb.Warning)
    create_db()
    import pdb; pdb.set_trace()  # XXX BREAKPOINT

