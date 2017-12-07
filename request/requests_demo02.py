# -*- coding: utf-8 -*-
import json
import requests

url = 'https://api.github.com'
imgURL = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1336155382,1942108681&fm=27&gp=0.jpg'

def build_uri(endpoint):
    return '/'.join([url, endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def download_image():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    response = requests.get(imgURL, headers=headers, stream=True)
    print response.status_code, response.reason
    print response.headers
    # print response.content  # 乱码
    # 将文件流写入指定文件
    with open('demo.jpg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)

def download_image_2():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    from contextlib import closing
    with closing(requests.get(imgURL, headers=headers, stream=True)) as response:   # 请求图片后将stream关闭
        with open('demo1.jpg', 'wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)

if __name__ == '__main__':
    download_image_2()