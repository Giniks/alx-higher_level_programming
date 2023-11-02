#!/bin/bash
# Sends a request to a URL and displays the size of the response body in bytes
echo "$(curl -sI "$1" | grep -i "Content-Length" | cut -d ' ' -f2) bytes"
