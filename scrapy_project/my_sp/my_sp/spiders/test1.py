from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from my_sp.items import MySpItem

class MySpider(CrawlSpider):
    name = "craigs"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/npo"]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        hxs = Selector(response)
        titles = hxs.xpath('//li[@class="result-row"]')
        items = []
        for titles in titles:
            item = CraigslistSampleItem()
            # item["title"] = titles.xpath("a/text()").extract()
            item["link"] = titles.xpath("a/@href").extract()
            # print("jhhj===========",titles.xpath("a/text()").extract())
            # print("title ===  ",titles.xpath("a/@href").extract())
            items.append(item)
        return(items)