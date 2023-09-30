#!/usr/bin/python3
"""This script thats Sends a POST request to a given URL with
given email.
Usage: ./2-post_email.py <URL> <email>
  - Also Displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    valuePost = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(valuePost).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
