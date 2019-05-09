from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from sqlite_database.items import SqliteDatabaseItem
import time
class MySpider(CrawlSpider):
    name = "craigs"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/npo"]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_items", follow= True),
    )
    # custom_settings={ 'FEED_URI': "aliexpress_%(time)s.json",
    #                    'FEED_FORMAT': 'json'}

    def parse_items(self, response):
        hxs = Selector(response)
        titles = hxs.xpath('//li[@class="result-row"]')
        # items = []
        index = 1
        item = SqliteDatabaseItem()

        for titles in titles:
            item["title"] = titles.xpath("p/a/text()").getall()
            item["link"] = titles.xpath("a/@href").extract()
            if index%2 == 0:
                item["name"] = "satish"
            else:
                item["name"] = ""
            index += 1 

            yield item  
            # items.append(item)
        # return(items)
