from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from my_sp.items import MySpItem
import time
class MySpider(CrawlSpider):
    name = "craigs"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/npo"]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_items", follow= True),
    )
    custom_settings={ 'FEED_URI': "aliexpress_%(time)s.json",
                       'FEED_FORMAT': 'json'}

    def parse_items(self, response):
        hxs = Selector(response)
        titles = hxs.xpath('//li[@class="result-row"]')
        items = []
        for titles in titles:
            item = MySpItem()
            item["title"] = titles.xpath("p/a/text()").getall()
            item["link"] = titles.xpath("a/@href").extract()
            items.append(item)
        return(items)
