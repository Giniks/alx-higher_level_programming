#!/bin/bash
# Sends a DELETE request to a URL and displays the body of the response
curl -sX DELETE "$1" && echo -e "\nI'm a DELETE request"
