# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BricksetItem(scrapy.Item):
    name = scrapy.Field()
    pieces = scrapy.Field()
    minifigs =  scrapy.Field()
    image = scrapy.Field()
    