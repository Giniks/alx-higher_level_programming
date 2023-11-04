#!/usr/bin/python3
"""
This is a Python script that makes use of Basic Authentication with a personal access token to access the GitHub API and display your user ID.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))

