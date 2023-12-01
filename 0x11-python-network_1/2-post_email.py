#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


if __name__ == '__main__':
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    import sys

    url, email = sys.argv[1], sys.argv[2]

    email_data = urlencode({'email': email}).encode('utf-8')
    request = Request(url, data=email_data, method='POST')

    with urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)
