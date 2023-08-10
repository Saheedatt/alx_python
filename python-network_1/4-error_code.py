#!/usr/bin/python3
import requests
import sys

def main():
    """
    Entry point of the script.
    Parses the command line arguments, sends a GET request to the specified URL,
    and displays the response body. If the status code is 400 or greater, an error
    message is displayed.

    Usage: python script_name.py <URL>
    """
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        return

    url = sys.argv[1]


    try:
        response = requests.get(url)
        print("Response body:")
        print(response.text)
        
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
