#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q', q}
    response = requests.post(url, data=payload)

    try:
        json_data = response.json()
        json_data_id = json_data.get('id', "")
        json_data_name = json_data.get('name', "")
        if json_data_id and json_data_name:
            print(f"[{json_data_id}] {json_data_name}")
        else:
            print("No result")
    except (ValueError, Exception):
        print("Not a valid JSON")
