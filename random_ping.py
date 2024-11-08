import requests
import random
import time
import os
import sys
from datetime import datetime


def ping_url(url):
    try:
        response = requests.get(url)
        print(f"[{datetime.now()}] Pinged {url} - Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"[{datetime.now()}] Failed to ping {url} - Error: {e}")


def run_random_ping(url):
    while True:
        # Generate a random number of seconds to wait (up to 3600 seconds, or 1 hour)
        wait_time = random.randint(1, 3600)
        print(f"Waiting for {wait_time} seconds before the next ping.")
        time.sleep(wait_time)

        # Ping the URL
        ping_url(url)


# Get URL from command-line argument or environment variable
url = sys.argv[1] if len(sys.argv) > 1 else os.getenv("PING_URL", "https://example.com")

if __name__ == "__main__":
    print(f"Starting to ping URL: {url}")
    run_random_ping(url)
