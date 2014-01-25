#!/usr/bin/env python

import urllib
import urllib2
import webbrowser

url = "http://duckduckgo.com/html"
data = urllib.urlencode({'q': 'Python'})
results = urllib2.urlopen(url, data)
with open("results.html", "w") as f:
    f.write(results.read())
webbrowser.open("results.html")
