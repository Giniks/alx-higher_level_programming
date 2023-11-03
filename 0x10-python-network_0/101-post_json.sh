#!/bin/bash
# srnds JSON POST request and displays the body of response
curl -sLX POST -H "Content-Type: application/json" -d @"$2" "$1"
