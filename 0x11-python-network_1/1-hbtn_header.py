#!/usr/bin/python3
'''script that takes in a URL, and diplays value
    of the X-Request-Id variable found in the header of the response
'''
import sys
import urllib.request
from urllib.request import urlopen

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
