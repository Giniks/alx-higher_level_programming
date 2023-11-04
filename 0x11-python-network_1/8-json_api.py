#!/usr/bin/python3
"""
This is a python Script that takes in letter
Sends a POST request to http://0.0.0.0:5000/search_user
With the letter as parameter and process response
"""


import requests
import sys

if __name__ == "__main":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}

    r = requests.post(url, data=data)

    try:
        json_data = r.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

