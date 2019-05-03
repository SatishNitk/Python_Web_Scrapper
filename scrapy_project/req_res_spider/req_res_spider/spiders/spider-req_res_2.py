from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
import time
from req_res_spider.items import ReqResSpiderItem
import scrapy
class MySpider(CrawlSpider):
    name = "req_res_sp1"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/npo"]


# getting second item value from second methos i.e   parse_page2

    def parse(self, response):
        self.logger.info("first parser")
        item = ReqResSpiderItem()
        item['main_url'] = response.url
        request =  scrapy.Request("https://sfbay.craigslist.org/search/npo?s=120",
                          callback=self.parse_page2)
        request.meta['items'] = item
        print(response.url)
        yield request

    def parse_page2(self, response):
        self.logger.info("second parser")
        self.logger.info("Visited %s", response.url)
        item = response.meta['items']
        item['other_url'] = response.url
        self.logger.info("item= {}".format(item['other_url']))

        yield item

        