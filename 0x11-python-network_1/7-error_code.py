#!/usr/bin/python3
"""This script Sends a request to a given URL
and displays response body.
Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    rSend = requests.get(url)
    if rSend.status_code >= 400:
        print("Error code: {}".format(rSend.status_code))
    else:
        print(rSend.text)
