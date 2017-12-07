# -*- coding: utf-8 -*-
import json
import requests
from requests import exceptions

url = 'https://www.facebook.com'

def build_uri(endpoint):
    return '/'.join([url, endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def proxy():
    proxies = {"http": "socks5://127.0.0.1:1080", "https": "socks5://127.0.0.1:1080"}
    try:
        response = requests.get(url, proxies=proxies, timeout=10)
    except exceptions.Timeout as e:
        print e
    else:
        print response.status_code
        print response.text

if __name__ == '__main__':
    proxy()