#!/bin/bash
# Sends a POST to URL with custom variables & displays the body of the response
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"

