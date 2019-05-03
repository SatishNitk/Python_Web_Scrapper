from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
import time
import scrapy
class MySpider(CrawlSpider):
    name = "req_res_sp"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/npo"]

    def parse(self, response):
        self.logger.info("first parser")
        return scrapy.Request("http://sfbay.craigslist.org/search/npo",
                          callback=self.parse_page2)

    def parse_page2(self, response):
        self.logger.info("second parser")
        self.logger.info("Visited %s", response.url)
        