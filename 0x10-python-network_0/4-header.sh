#!/bin/bash
# Sends a GET request to a URL with a custom header & displays the response bod
curl -sH "X-School-User-Id: 98" "$1"
