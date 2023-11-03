#!/bin/bash
# Makes a request to the server to get the response containing "You got me!"
curl -sL -H "0.0.0.0:5000/catch_me" "Origin:School" -X PUT -d "user_id=98"
