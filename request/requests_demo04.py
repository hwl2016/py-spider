# -*- coding: utf-8 -*-
import json
import requests
from requests import exceptions

url = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([url, endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def basic_auth():
    response = requests.get(build_uri('user'), auth=('imoocdemo', 'imoocdemo123'))
    print response.request.headers  # 'Authorization': 'Basic aW1vb2NkZW1vOmltb29jZGVtbzEyMw=='
    print better_print(response.text)

def basic_oauth():
    headers = {
        "Authorization": "token 2cfdd24a0d4e33a47c101101bcc3d3e290c36e2b"
    }
    response = requests.get(build_uri('user/emails'), headers=headers)
    print response.request.headers
    print better_print(response.text)

from requests.auth import AuthBase

class GithubAuth(AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers['Authorization'] = ' '.join(['token', self.token])
        return r

def oauth_advanced():
    auth = GithubAuth('2cfdd24a0d4e33a47c101101bcc3d3e290c36e2b')
    response = requests.get(build_uri('user/emails'), auth=auth)
    print response.request.headers
    print better_print(response.text)

if __name__ == '__main__':
    oauth_advanced()