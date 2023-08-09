#!/usr/bin/python3
"""
GitHub User ID Script

This script takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user ID.

Usage: python github_user_id.py <username> <personal_access_token>
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

def get_user_id(username, personal_access_token):
    """
    Fetches the user ID using GitHub API with Basic Authentication.

    Args:
        username (str): GitHub username.
        personal_access_token (str): Personal access token for authentication.
    """
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(username, personal_access_token)

    try:
        response = requests.get(url, auth=auth)

        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data.get("id")
            
            if user_id is not None:
                print(f"User ID: {user_id}")
            else:
                print("Unable to fetch user ID.")
        else:
            print(f"Request failed with status code: {response.status_code}")
            print("Response content:", response.content)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python github_user_id.py <username> <personal_access_token>")
    else:
        username = sys.argv[1]
        personal_access_token = sys.argv[2]
        get_user_id(username, personal_access_token)
