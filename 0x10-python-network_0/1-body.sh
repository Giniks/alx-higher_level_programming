#!/bin/bash
# Sends a GET request to a URL, displays the body of a 200 status code response
{ curl -sL "$1"; echo; }
