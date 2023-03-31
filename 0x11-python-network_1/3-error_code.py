#!/usr/bin/python3
'''script that takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8).
'''
import sys
from urllib.error import HTTPError
from urllib.request import urlopen
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
