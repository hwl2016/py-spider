# -*- coding: utf-8 -*-
import urllib2, urllib

url = 'https://api.github.com/users/hwl2016'

def use_simple_urllib2():
    response = urllib2.urlopen(url)
    print '>>>Response Headers:'
    print response.info()
    print '>>>Response Body:'
    print ''.join([line for line in response.readlines()])

def use_params_urllib2():
    # 构建请求参数
    data = {
        'a': 'aaa',
        'b': 'bbb'
    }
    params = urllib.urlencode(data)
    print 'Request Params:'
    print params
    # 发送请求
    response = urllib2.urlopen('?'.join([url, '%s']) % params)
    # 处理相应
    print '>>>Response Headers:'
    print response.info()
    print '>>>Status Code:'
    print response.getcode()
    print '>>>Response Body:'
    print ''.join([line for line in response.readlines()])


if __name__ == '__main__':
    print '>>>Use Simple urllib2:'
    use_simple_urllib2()
    print '>>>Use Params urllib2:'
    use_params_urllib2()