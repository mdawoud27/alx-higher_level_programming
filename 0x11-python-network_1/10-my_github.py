#!/usr/bin/python3
"""Write a Python script that takes GitHub acc
credentials (username and password) and uses the GitHub API to display your id
"""


if __name__ == '__main__':
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    auth = (username, password)
    response = requests.get(url, auth=auth)

    try:
        data = response.json()
        print(data.get('id'))
    except (ValueError, Exception):
        print(None)
