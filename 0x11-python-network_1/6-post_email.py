#!/usr/bin/python3
"""
This Python script that takes a URL and an email address.
Sends a POST request to the URL with the email as a parameter
And displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    r = requests.post(url, data=data)

    print(r.text)

