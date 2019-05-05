# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImageDownloadItem(scrapy.Item):
    # define the fields for your item here like:
    # images = scrapy.Field()

    #image urls this should be the name only 
    image_urls = scrapy.Field()
