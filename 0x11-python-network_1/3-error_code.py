#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""


if __name__ == '__main__':
    import sys
    from urllib.request import urlopen
    from urllib.error import HTTPError

    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            body = response.read().decode('utf-8')
    except HTTPError as error:
        print(f"Error code: {error.code}")
