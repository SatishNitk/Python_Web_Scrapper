# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class MySpPipeline(object):
    def process_item(self, item, spider):
        if item.get("name") == "satish":
            item["name"] = "kumargupta"
            return item
        else:
            raise DropItem("Missing price in %s" % item)
class MySpPipeline_second(object):
    def process_item(self, item, spider):
        if item.get("name") == "kumargupta":
            item["name"] = "satishkumargupta"
            return item
        else:
            raise DropItem("Missing price in %s" % item)
        
