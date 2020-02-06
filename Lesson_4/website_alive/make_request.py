import requests


def make_re(c):
    req = requests.get(c)
    return req.status_code
