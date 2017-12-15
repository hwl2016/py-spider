# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_demo.scrapy_demo.items import ScrapyDemoItem


class CountrySpider(CrawlSpider):
    name = 'country'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/', deny=r'/user/'), follow=True),
        Rule(LinkExtractor(allow=r'places/default/view/', deny=r'/user/'), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        i = ScrapyDemoItem()
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        i['name'] = response.css('tr#places_country__row td.w2p_fw::text').extract()
        i['population'] = response.css('tr#places_population__row td.w2p_fw::text').extract()
        return i
