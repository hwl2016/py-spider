# encoding: UTF-8

from link_crawler import *
import re
from bs4 import BeautifulSoup
import lxml.html
import time

# 三种方式抓取页面数据性能比较
FIELDS = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld',
          'currency_code', 'currency_name', 'phone', 'postal_code_format',
          'postal_code_regex', 'languages', 'neighbours')

# 1、正则
def re_scraper(html):
    results = {}
    for field in FIELDS:
        results[field] = re.search('<tr id="places_%s__row">.*?<td class="w2p_fw">(.*?)</td>' % field, html).groups()[0]
    return  results

# 2、BeautifulSoup
def bs_scraper(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = {}
    for field in FIELDS:
        results[field] = soup.find('table').find('tr', id="places_%s__row" % field).find('td', class_="w2p_fw").text
    return results

# 3、lxml
def lxml_scraper(html):
    tree = lxml.html.fromstring(html)
    results = {}
    for field in FIELDS:
        results[field] = tree.cssselect('tr#places_%s__row td.w2p_fw' % field)[0].text_content()
    return results

def get_counter():
    NUM_ITERATIONS = 1000
    url = 'http://example.webscraping.com/places/default/view/United-Kingdom-239'
    html = download(url, {'User-agent': 'GoodAgent'}, None, 2)

    for name, scraper in [('Regex', re_scraper), ('BeautifulSoup', bs_scraper), ('Lxml', lxml_scraper)]:
        start = time.time()
        for i in range(NUM_ITERATIONS):
            if scraper == re_scraper:
                re.purge()  # 清空re缓存
            result = scraper(html)
            assert(result['area'] == '244,820 square kilometres')
        end = time.time()
        print '%s: %.2f seconds' % (name, end - start)

# https://bitbucket.org/wswp/code/src/tip/chapter02/linkcrawler.py

if __name__ == '__main__':
    get_counter()
