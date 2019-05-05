# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

import logging
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher


class MySpPipeline(object):
    def process_item(self, item, spider):
        logging.log(logging.WARNING, "This is a warning: first pipeline started")

        if item.get("name") == "satish":
            item["name"] = "kumargupta"
            return item
        else:
            raise DropItem("Missing price in %s" % item)
class MySpPipeline_second(object):
    def __init__(self):
        dispatcher.connect(self.spider_opened, signal=signals.spider_opened)
        dispatcher.connect(self.spider_closed, signal = signals.spider_closed)

    def spider_opened(self, spider):
        logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        

    def process_item(self, item, spider):
        logging.log(logging.WARNING, "This is a warning: second pipeline started")

        if item.get("name") == "kumargupta":
            item["name"] = "satishkumargupta"
            return item
        else:
            raise DropItem("Missing price in %s" % item)
    def spider_closed(self, spider):
        logging.log(logging.WARNING, "This is a warning: closing------------------------------------------------------")
        logging.log(logging.WARNING, "This is a warning: closing secong-------------------------------------------------------------------------------------------------------------")

