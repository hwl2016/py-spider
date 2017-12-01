# encoding: UTF-8

from link_crawler import *
import re
from bs4 import BeautifulSoup
import lxml.html

url = 'http://example.webscraping.com/places/default/view/Antarctica-9'

html = download(url, {'User-agent': 'GoodAgent'}, None, 2)

# 正则表达式匹配网页内容
res = re.findall('<td class="w2p_fw">(.*?)</td>', html)

for item in res:
    print item

print '#####################'

# Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
tr = soup.find(attrs={'id': 'places_area__row'})
td = tr.find(attrs={'class': 'w2p_fw'})
area = td.text
print area

# Lxml
tree = lxml.html.fromstring(html)
td2 = tree.cssselect('tr#places_area__row .w2p_fw')[0]
area2 = td2.text_content()
print area2
