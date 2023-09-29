#!/bin/bash
# This script sends request to URL with curl, and displays size of the body of response
curl -s "$1" | wc -c
