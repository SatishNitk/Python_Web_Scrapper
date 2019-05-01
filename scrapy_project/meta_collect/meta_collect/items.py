# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MetaCollectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    cscore  = scrapy.Field()
    uscore = scrapy.Field()
    date = scrapy.Field()
    desc = scrapy.Field()


# from scrapy.item import Item, Field
# class MetacriticItem(Item):
#     '''
#     Class for the item retrieved by scrapy.
#     '''
#     # Here are the fields that will be crawled and stored
#     title = Field() # Game title
#     link = Field()  # Link to individual game page
#     cscore = Field() # Critic score
#     uscore = Field()   # User score
#     date = Field()  # Release date
#     desc = Field()  # Description of game