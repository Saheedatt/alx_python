#!/usr/bin/python3

"""
Search User Script

This script takes a letter as input and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
It processes the response based on JSON formatting and content.

Usage: python search_user.py <letter>
"""

import sys
import requests

def search_user(letter):
    """
    Sends a POST request to search for a user based on the provided letter.

    Args:
        letter (str): The letter to use as a search parameter.
    """
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}

    try:
        response = requests.post(url, data=data)
        json_data = response.json()

        if isinstance(json_data, dict) and json_data:
            user_id = json_data.get("id", "N/A")
            user_name = json_data.get("name", "N/A")
            print(f"[{user_id}] {user_name}")
        elif not json_data:
            print("No result")
        else:
            print("Not a valid JSON")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
