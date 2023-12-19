import requests
import os

def get_json(url):
    return requests.get(url).json()


def get_os_user_lower():
    username = os.getenv("USER")
    
    if username is None:
        raise ValueError("No user set")
    
    return username.lower()