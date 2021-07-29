import signal

from contextlib import contextmanager

import requests
import os
import json


DELAY = INTERVAL = 4 * 60  # interval time in seconds
MIN_DELAY = MIN_INTERVAL = 2 * 60

PATH_DIR = os.getcwd()
SECRETS_PATH = os.path.join(PATH_DIR, 'secrets.json') # secrets.json 파일 위치를 명시

KEEP_ALIVE_TOKEN = get_secret("KEEP_ALIVE_TOKEN", json.loads(open(SECRETS_PATH).read()))
KEEPALIVE_URL = "https://nebula.udacity.com/api/v1/remote/keep-alive"
TOKEN_URL = "http://metadata.google.internal/computeMetadata/v1/instance/attributes/"+KEEP_ALIVE_TOKEN
TOKEN_HEADERS = {"Metadata-Flavor":"Google"}


def get_secret(setting, secrets=secrets):
    """
    Get a secret variable or return an explicit exception.
    """

    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        print(error_msg)

def _request_handler(headers):
    def _handler(signum, frame):
        requests.request("POST", KEEPALIVE_URL, headers=headers)
    return _handler


@contextmanager
def active_session(delay=DELAY, interval=INTERVAL):
    """
    Example:

    from workspace_utils import active session

    with active_session():
        # do long-running work here
    """
    print("start context manager")
    print(KEEP_ALIVE_TOKEN)
    token = requests.request("GET", TOKEN_URL, headers=TOKEN_HEADERS).text
    print("successively get token")
    headers = {'Authorization': "STAR " + token}
    delay = max(delay, MIN_DELAY)
    interval = max(interval, MIN_INTERVAL)
    original_handler = signal.getsignal(signal.SIGALRM)
    try:
        signal.signal(signal.SIGALRM, _request_handler(headers))
        signal.setitimer(signal.ITIMER_REAL, delay, interval)
        yield
    finally:
        signal.signal(signal.SIGALRM, original_handler)
        signal.setitimer(signal.ITIMER_REAL, 0)


def keep_awake(iterable, delay=DELAY, interval=INTERVAL):
    """
    Example:

    from workspace_utils import keep_awake

    for i in keep_awake(range(5)):
        # do iteration with lots of work here
    """
    with active_session(delay, interval): yield from iterable