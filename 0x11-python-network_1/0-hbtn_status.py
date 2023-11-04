#!/usr/bin/python3
"""
This is a python script that summons https://alx-intranet.hbtn.io/status using urllib
And displays information about the response body.
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        body_content = response.read()

        print("Body response:")
        print(f"    - type: {type(body_content)}")
        print(f"    - content: {body_content}")
        print(f"    - utf8 content: {body_content.decode('utf-8')}")
