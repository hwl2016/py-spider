# -*- coding: utf-8 -*-

# pip install builtwith  识别网站所用的技术
# >>>import builtwith
# >>>builtwith.parse('http://www.up-id.com')

# pip install python-whois  寻找网站所有者
# >>>import whois
# >>>print whois.whois('baidu.com')


import urllib2
import urlparse
import re
import itertools
import robotparser
import datetime
import time

# 解析 robots.txt
rp = robotparser.RobotFileParser()
rp.set_url('http://example.webscraping.com/robots.txt')
rp.read()

# 下载网页
def download(url, num_retries=2):
    print 'Downloading', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # 服务器端报错 5xx 时重新加载
                return download(url, num_retries-1)
    return html

# 设置用户代理
def download2(url, user_agent='wswp', proxy=None, num_retries=2):
    print 'Downloading', url
    headers = {
        'User-Agent': user_agent
    }
    request = urllib2.Request(url, headers=headers)

    # 设置proxy
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))

    try:
        # html = urllib2.urlopen(request).read()
        html = opener.open(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # 服务器端报错 5xx 时重新加载
                return download2(url, user_agent, proxy, num_retries-1)
    return html

# print download('http://www.up-id.com')
# print download('http://httpstat.us/500')
# print download2('http://www.meetup.com')


# 网站地图爬虫
def crawl_sitemap(url):
    sitemap = download(url)
    # 抽取超链接
    links = re.findall('<a href=">(.*?)">', sitemap)
    for link in links:
        html = download('http://example.webscraping.com' + link)

# crawl_sitemap('http://example.webscraping.com/')

# 遍历ID爬取
# max_errors = 5
# num_errors = 0
# for page in itertools.count(1):
#     url = 'http://example.webscraping.com/places/default/view/%s' % page
#     html = download(url)
#     if html is None:
#         num_errors += 1
#         if num_errors == max_errors:
#             break
#     else:
#         num_errors = 0


# 链接爬虫

### 高级功能
### 1、解析robots.txt  robotparser 模块
'''
rp = robotparser.RobotFileParser()
rp.set_url('http://example.webscraping.com/robots.txt')
rp.read()
url = 'http://example.webscraping.com'
user_agent = 'BadCrawler'
print rp.can_fetch(user_agent, url)

user_agent = 'GoodCrawler'
print rp.can_fetch(user_agent, url)
'''

### 2、支持代理



def link_crawler(seed_url, link_regex, user_agent='wswp', max_depth=2):
    crawler_queue = [seed_url]
    # 对crawl_queue去重
    seen = set(crawler_queue)

    while crawler_queue:
        url = crawler_queue.pop()
        if rp.can_fetch(user_agent, url):   # 添加robots.txt解析
            html = download2(url, user_agent)
            # 过滤页面符合条件的链接
            for link in get_links(html):
                if re.match(link_regex, link):
                    link = urlparse.urljoin(seed_url, link)  # 创建绝对路径
                    # 查看link是否已经被添加过了
                    if link not in seen:
                        seen.add(link)
                        crawler_queue.append(link)
        else:
            print 'Block by robots.txt:', url


def get_links(html):
    # 返回页面所有链接
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)

link_crawler('http://example.webscraping.com/', '(.*?)view(.*?)', 'BadCrawler')




### 3、下载限速
# Throttle 记录了每个域名上次访问的时间，如果当前时间距离上次访问时间小于指定延时，则执行睡眠操作。我们可以在每次下载之前调用Throttle对爬虫进行限速
class Throttle:
    # 两次下载之间添加延时
    def __init__(self, delay):
        self.delay = delay
        self.domains = {}

    def wait(self, url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domain.get(domain)

        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.datetime.now()

### 4、避免爬虫陷阱
"""
    一些网站会动态生成页面内容， 这样就会出现无限多的网页。比如，网站有一个在线日历功能，
提供了可以访问下个月和下一年的链接，那么下个月的页面中同样会包含访问再下个月的链接，
这样页面就会无止境地链接下去。这种情况被称为爬虫陷阱。
    想要避免陷入爬虫陷阱，一个简单的方法是记录到达当前网页经过了多少个链接，也就是深度。
当到达最大深度时，爬虫就不再向队列中添加该网页中的链接了

https://bitbucket.org/wswp/code/src/tip/chapter01/link_crawler3.py
"""