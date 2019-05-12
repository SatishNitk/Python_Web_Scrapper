# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GotProjectItem(scrapy.Item):
	name  = scrapy.Field()
	image_urls = scrapy.Field()   # it contains only list check to spider
