#!/usr/bin/python3

"""
Module to fetch and display the value of the X-Request-Id variable in the response header of a given URL
"""


import requests
import sys

def fetch_and_display_x_request_id(url):
    """
    Fetches the value of X-Request-Id variable in the response
    header of the given URL and displays it.
    """
    response = requests.get(url)
    if response.ok:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id is not None:
            print(x_request_id)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)
    
    url = sys.argv[1]
    fetch_and_display_x_request_id(url)
