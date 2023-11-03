#!/bin/bash
# Sends a GET request to a URL and displays the body of a 200 status code response
curl -s "$1" -w "\n%{http_code}" | awk -F"\n" 'NF>1{print $1}'
