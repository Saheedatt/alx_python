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
        user_data = response.json()

        if "id" in user_data:
            print(f"User ID: {user_data['id']}")
        else:
            print("Unable to fetch user ID.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    username = sys.argv[1]
    personal_access_token = sys.argv[2]
    get_user_id(username, personal_access_token)
