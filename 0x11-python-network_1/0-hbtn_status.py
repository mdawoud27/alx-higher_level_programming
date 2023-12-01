#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == '__main__':
    import urllib.request as url_req

    url = 'https://alx-intranet.hbtn.io/status'

    with url_req.urlopen(url) as response:
        content = response.read()

    print("Body response:")
    print(f"   - type: {type(content)}")
    print(f"   - content: {content}")
    print(f"   - utf8 content: {content.decode('utf-8')}")
