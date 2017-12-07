# -*- coding: utf-8 -*-
import json
import requests
from requests import exceptions

url = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([url, endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def request_method():
    # response = requests.get(build_uri('users/hwl2016'))
    # print better_print(response.text)
    # 带认证参数的请求
    response = requests.get(build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'))
    print better_print(response.text)

# GET 参数请求
def params_request():
    response = requests.get(build_uri('users'), params={"since": 135})
    print better_print(response.text)
    print response.request.headers
    print response.url  # https://api.github.com/users?since=135

# json 参数提交
def json_request():
    response = requests.patch(build_uri('user'), auth=('imoocdemo', 'imoocdemo123'), json={"name": "haha_michael"})
    print better_print(response.text)
    print response.request.headers
    print response.request.body
    print response.status_code  # 422
    print response.url  # https://api.github.com/user

def timeout_request():
    try:
        response = requests.get(build_uri('user/emails'), timeout=10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print e.message
    except exceptions.HTTPError as e:
        print e.message
    else:
        print better_print(response.text)
        print response.status_code

# 自定义request请求
def hard_request():
    from requests import Request, Session
    s = Session()
    headers = {"User-Agent": "aaa"}
    req = Request('GET', build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'), headers=headers)
    # 准备请求
    prepared = req.prepare()
    print prepared.headers
    print prepared.body

    # 发送请求
    res = s.send(prepared, timeout=10)
    print res.status_code
    print res.request.headers
    print better_print(res.text)

if __name__ == '__main__':
    hard_request()