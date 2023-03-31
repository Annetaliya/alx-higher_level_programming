#!/usr/bin/python3
''' Python script that fetches https://alx-intranet.hbtn.io/status'''

import json
from urllib.request import urlopen
if __name__ == "__main__":
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()
items = body
print("Body response:")
print('\t- type: {}'.format(type(items)))
print('\t- content: {}'.format(items))
print('\t- utf8 content: {}'.format(items.decode('utf-8')))
