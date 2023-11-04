#!/usr/bin/python3
"""
This is a script that fetches url, Send request and displays the body response.
print: Error code: if the  HTTP status code is greater than or equal to 400.
Followed by the HTTP status codr.
"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    r = request.get(url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)

