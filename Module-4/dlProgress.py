#!/usr/bin/env python

import sys, urllib, getopt, time

def usage():
        print "Usage: ./dlProgress.py <url1> <url2> ... <urln>"

def main(argv):
        try:
                opts, args = getopt.getopt(argv, "h")
        except getopt.GetoptError:
                usage()
                sys.exit(2)
        for opt, arg in opts:
                if opt in ("-h"):
                        usage()
                        sys.exit()
        if len(args) < 1:
                usage()
                sys.exit(2)
        i = 1
        for url in args:
                print "Downloading: ", url
                try:
                        urllib.urlretrieve(url, str(i), reporthook=dlProgress)
                except:
                        print "Error during download of ",url
                i += 1

def dlProgress(count, blockSize, totalSize):
        percent = int(count*blockSize*100/totalSize)
        sys.stdout.write("%2d%%" % percent)
        sys.stdout.write("\b\b\b")
        sys.stdout.flush()

if __name__ == "__main__":
        main(sys.argv[1:])
