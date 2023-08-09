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
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for non-200 status codes
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id is not None:
            print(x_request_id)
        else:
            print("No X-Request-Id header found in response")
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)
    
    url = sys.argv[1]
    fetch_and_display_x_request_id(url)



import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        return

    url = sys.argv[1]

    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')

        if x_request_id:
            print(f"X-Request-Id value: {x_request_id}")
        else:
            print("X-Request-Id header not found in the response.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
