# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FileDownloadItem(scrapy.Item):
    # define the fields for your item here like:
    file_urls = scrapy.Field()
    files = scrapy.Field()  #its a optional.... nothing harmful to keep .. some concept is there but let me find ..the concept

