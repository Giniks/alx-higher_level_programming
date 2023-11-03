#!/bin/bash
# Sends an OPTIONS request to a URL and displays the allowed HTTP methods
curl -sI "$1" | grep "Allow" | cut -d ' ' -f2-
