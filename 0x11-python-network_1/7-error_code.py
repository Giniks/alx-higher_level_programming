#!/usr/bin/python3
"""
This is a script that fetches url, Send request and displays the body response
print: Error code: if the  HTTP status code is greater than or equal to 400
Followed by the HTTP status code
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
