#!/usr/bin/python3
"""
This is Python script that fetches https://alx-intranet.hbtn.io/status
Using the requests package.
And displays information about the response body.
"""

import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
