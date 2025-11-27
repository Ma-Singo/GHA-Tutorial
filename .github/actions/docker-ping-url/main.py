import os
import requests
from time import sleep

def ping_url(url, max_trials, delay):
    trials = 0

    while trials < max_trials:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Website {url} is reachable")
            return True
        except requests.ConnectionError():
            print(f"Website {url} is unreachable")

        finally:
            trials += 1
            sleep(delay)

def run():
    website_url = os.getenv("INPUT_URL")
    max_trials = int(os.getenv("INPUT_MAX_TRIALS"))
    delay = int(os.getenv("INPUT_DELAY"))

    ping_url(website_url, max_trials, delay)



if __name__ == "__main__":
    print("Hello World!")