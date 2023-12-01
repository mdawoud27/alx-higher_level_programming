#!/usr/bin/python3

if __name__ == '__main__':
    import urllib.request as url_req
    import sys

    url = sys.argv[1]
    with url_req.urlopen(url) as response:
        header_value = response.getheader('X-Request-Id')
        print(header_value)
