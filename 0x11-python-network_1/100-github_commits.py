#!/usr/bin/python3
"""This script Lists 10 most recent commits
on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    rGit = requests.get(url)
    commits = rGit.json()
    try:
        for z in range(10):
            print("{}: {}".format(
                commits[z].get("sha"),
                commits[z].get("commit").get("author").get("name")))
    except IndexError:
        pass
