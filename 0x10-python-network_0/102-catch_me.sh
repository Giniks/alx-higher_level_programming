#!/bin/bash
# Makes a request to the server to get the response containing "You got me!"
curl -sLX PUT -d 'user_id=98' "You got me!" -H 'Origin:School' "0.0.0.0:5000/catch_me"
