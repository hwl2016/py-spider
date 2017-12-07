# -*- coding: utf-8 -*-
import requests

url = 'https://api.github.com/users/hwl2016'

def use_simple_requests():
    response = requests.get(url)
    print '>>>Response Headers:'
    print response.headers
    print '>>>Response Body:'
    print response.text

def use_params_requests():
    data = {
        'a': 'aaa',
        'b': 'bbb'
    }
    # 发送请求
    response = requests.get(url, params=data)
    # 处理相应
    print '>>>Response Headers:'
    print response.headers
    print '>>>Status Code:'
    print response.status_code
    print '>>>Response Body:'
    print response.json()

if __name__ == '__main__':
    print '>>>Use Simple requests:'
    use_simple_requests()
    print '>>>Use Params requests:'
    use_params_requests()