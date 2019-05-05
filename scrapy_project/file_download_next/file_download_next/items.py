# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose

def remove_space(value):
	# return value.strip("-")[1]   # get value after -
	return value

class FileDownloadItem(scrapy.Item):
    # define the fields for your item here like:
    file_urls = scrapy.Field()
    files = scrapy.Field()  #its a optional.... nothing harmful to keep .. some concept is there but let me find ..the concept
    file_name = scrapy.Field(
    	input_processor = MapCompose(remove_space),
    	output_processor = TakeFirst()
    	)
    
