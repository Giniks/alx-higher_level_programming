#!/usr/bin/python3
"""
This is Python script that fetches https://alx-intranet.hbtn.io/status using the requests package.
And displays information about the response body.
"""

import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

print("Body response:")
print(f"    - type: {type(response.text)}")
print(f"    - content: {response.text}")

