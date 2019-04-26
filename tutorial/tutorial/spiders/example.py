# -*- coding: utf-8 -*-
import scrapy
from ..items import ItemWord


class ExampleSpider(scrapy.Spider):
    name = "start"
    start_urls = ['http://www.english-bangla.com/browse/index/a']

    def parse(self, response):
        all_char = response.css('div.a-z>a::attr(href)').extract()
        for char in all_char:
            yield scrapy.Request(url=char, callback=self.next_page)

    def next_page(self, response):
        urls = response.css("div#cat_page>ul>li>a::attr(href)").getall()
        for url in urls:
            url=response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)
        next_page_url = response.css('div.pagination>a[rel=next]::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.next_page)

    def parse_details(self, response):
        dictionary = ItemWord()
        eng_word = response.css('span#speak.word::text').get().strip()
        ban_mean = response.css('span.format1::text').get().replace(u'\ax0', u' ').strip()
        dictionary['eng_word'] = eng_word
        dictionary['ban_mean'] = ban_mean
        yield dictionary
