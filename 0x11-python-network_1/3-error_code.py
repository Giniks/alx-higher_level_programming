#!/usr/bin/python3
"""
This is a python script that takes a URL, sends a request to the URL
And displays the body of the response (decoded in utf-8).
Handles urllib.error.HTTPError exceptions and prints the HTTP status code.
"""

import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
