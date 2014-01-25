#!/usr/bin/env python

import requests

url = "http://duckduckgo.com/html"
payload = {'q':'python'}
r = requests.post(url, payload)
with open("requests_results.html", "w") as f:
    f.write(r.content)
