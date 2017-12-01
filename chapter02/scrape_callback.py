# -*- coding: utf-8 -*-

import csv
import re
import urlparse
import lxml.html
from link_crawler import link_crawler

FIELDS = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code',
          'currency_name', 'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')


def scrape_callback(url, html):
    if re.search('/view/', url):
        tree = lxml.html.fromstring(html)
        # 列表生成式
        row = [tree.cssselect('table > tr#places_{}__row > td.w2p_fw'.format(field))[0].text_content() for field in FIELDS]
        print url, row

class ScrapeCallback:
    def __init__(self):
        self.writer = csv.writer(open('countries.csv', 'w'))
        self.fields = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code',
                       'currency_name', 'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')
        self.writer.writerow(self.fields)

    def __call__(self, url, html):
        if re.search('/view/', url):
            tree = lxml.html.fromstring(html)
            row = []
            for field in self.fields:
                row.append(tree.cssselect('table > tr#places_{}__row > td.w2p_fw'.format(field))[0].text_content())
            self.writer.writerow(row)


if __name__ == '__main__':
    try:
        # 传递方法
        # link_crawler('http://example.webscraping.com/', '/places/default/view(.*?)', scrape_callback=scrape_callback)
        # 传递类
        link_crawler('http://example.webscraping.com/', '/places/default/view(.*?)', scrape_callback=ScrapeCallback())
    except IndexError as e:
        print 'Error:', e
