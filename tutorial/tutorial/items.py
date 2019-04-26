# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItemWord(scrapy.Item):
    # define the fields for your item here like:
    eng_word = scrapy.Field()
    ban_mean = scrapy.Field()

    pass