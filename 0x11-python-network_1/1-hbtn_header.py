#!/usr/bin/python3
"""
A Python script that takes and send  request to the URL.
And displays the value of the X-Request-Id variable in the header of response
"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.info()
        x_request_id = header.get('X-Request-Id')
        if x_request_id is not None:
            print(x_request_id)
