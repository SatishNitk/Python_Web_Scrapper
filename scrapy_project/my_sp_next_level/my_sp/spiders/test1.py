from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from my_sp.items import MySpItem
from scrapy.loader import ItemLoader

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
        l = ItemLoader(item=MySpItem(), response=response)
        titles = hxs.xpath('//li[@class="result-row"]')
        index = 1
        for titles in titles:
            l.add_xpath("title",titles.xpath("p/a/text()").getall())
            l.add_xpath("link",titles.xpath("a/@href").extract())
            if index%2 == 0:
                l.add_value("name","satish")
            else:
                l.add_value("name", "")
            index += 1  
        return l.load_item()    
