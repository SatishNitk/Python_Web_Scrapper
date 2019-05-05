# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from scrapy.mail import MailSender

class MySpPipeline(object):
    # def spider_opened(self, spider):
    #     log.msg("opened spider  %s at time %s" % (spider.name,datetime.now().strftime('%H-%M-%S')))

    def process_item(self, item, spider):
        if item.get("name") == "satish":
            item["name"] = "kumargupta"
            return item
        else:
            raise DropItem("Missing price in %s" % item)

    # def spider_closed(self, spider):
    #     log.msg("closed spider %s at %s" % (spider.name,datetime.now().strftime('%H-%M-%S')))


class MySpPipeline_second(object):

    def process_item(self, item, spider):
        if item.get("name") == "kumargupta":
            item["name"] = "satishkumargupta"
            return item
        else:
            raise DropItem("Missing price in %s" % item)


    # mailer = MailSender()
    # mailer.send(to=["someone@example.com"], subject="Some subject", body="Some body", cc=["another@example.com"])
        
        


# def __init__(self):
        # dispatcher.connect(self.spider_opened, signal=signals.spider_opened)
        # dispatcher.connect(self.spider_closed, signal=signals.spider_closed)



