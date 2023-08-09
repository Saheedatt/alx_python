#!/usr/bin/python3
"""
Fetch and Display Response Script

This script takes a URL as input, sends a request to the URL,
and displays the body of the response. If the HTTP status code
is greater than or equal to 400, it prints an error message with
the status code.

Usage: python fetch_response.py <URL>
"""

import sys
import requests
from requests.exceptions import RequestException

def fetch_and_display_response(url):
    """
    Fetches the response from the provided URL and displays it.
    If the status code is 400 or higher, prints an error message.

    Args:
        url (str): The URL to send the request to.
    """
    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_response.py <URL>")
    else:
        url = sys.argv[1]
        fetch_and_display_response(url)
