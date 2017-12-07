# -*- coding: utf-8 -*-
import json
import requests
from requests import exceptions

url = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([url, endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def get_key_info(response, *args, **kwargs):
    """回调函数
    """
    print response.headers["Content-Type"]

def main():
    """主程序
    """
    requests.get(build_uri('user/hwl2016'), hooks=dict(response=get_key_info))  # 事件钩子


if __name__ == '__main__':
    main()