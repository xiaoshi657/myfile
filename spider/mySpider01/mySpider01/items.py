# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Myspider01Item(scrapy.Item):
    # define the fields for your item here like:
    # salary = scrapy.Field()
    # title = scrapy.Field()
    content = scrapy.Field()
