import logging
import os
import random
import sys
import time

import requests

logging.basicConfig(level=logging.INFO)

def ping_url(url):
    try:
        response = requests.get(url)
        logging.info(f"Pinged {url} - Status Code: {response.status_code}")
    except requests.RequestException as e:
        logging.info(f"Failed to ping {url} - Error: {e}")

def run_random_ping(url, interval):
    while True:
        wait_time = random.randint(1, interval)
        logging.info(f"Waiting for {wait_time} seconds before the next ping.")
        time.sleep(wait_time)
        ping_url(url)

url = sys.argv[1] if len(sys.argv) > 1 else os.getenv("PING_URL", "http://localhost:3000")
interval = int(sys.argv[2]) if len(sys.argv) > 2 else int(os.getenv("PING_INTERVAL", 3600))

if __name__ == "__main__":
    logging.info(f"Starting to ping URL: {url} with a max interval of {interval} seconds.")
    run_random_ping(url, interval)
