#!/bin/bssh
# srnds JSON POST request and displays the body of response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1" | sed 'N;$!P;D'
