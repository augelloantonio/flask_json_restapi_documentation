import requests
import json
from urllib.parse import urlparse

# Correct API endpoint
endpoint = "https://www.augellotech.com"  # Ensure the full path is included
parsed_url = urlparse(endpoint)
domain = parsed_url.netloc
path = parsed_url.path or "/"  # Ensure path is never empty

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

try:
    # Use requests to send a GET request
    response = requests.get(endpoint, headers=headers)

except requests.RequestException as e:
    print(f"Error making API request: {e}")