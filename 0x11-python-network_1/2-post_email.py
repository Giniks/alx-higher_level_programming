#!/usr/bin/python3
"""
This python script takes in url and email and sends a POST request to the url.
with email as parameter abd displays body of response.
"""


import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    try:
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')
        req = urllib.request.Request(url, data)

        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
