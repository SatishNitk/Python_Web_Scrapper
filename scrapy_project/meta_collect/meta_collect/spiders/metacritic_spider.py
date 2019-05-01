import scrapy
from scrapy.selector import HtmlXPathSelector
from meta_collect.items import MetaCollectItem
class MetacriticSpider(scrapy.Spider):
    name = "metacritic" # Name of the spider, to be used when crawling
    allowed_domains = ["metacritic.com"] # Where the spider is allowed to go
    start_urls = [
        "http://www.metacritic.com/browse/games/title/pc?page=0"
    ]
    def parse(self, response):
        hxs = HtmlXPathSelector(response) # The XPath selector
        sites = hxs.select('//li[contains(@class, "product game_product")]/div[@class="product_wrap"]')
        items = []
        for site in sites:
        #     item = MetacriticItem()
        #     item['title'] = site.select('div[@class="basic_stat product_title"]/a/text()').extract()
        #     item['link'] = site.select('div[@class="basic_stat product_title"]/a/@href').extract()
        #     item['cscore'] = site.select('div[@class="basic_stat product_score brief_metascore"]/div/div/span[contains(@class, "data metascore score")]/text()').extract()
        #     item['uscore'] = site.select('div[@class="more_stats condensed_stats"]/ul/li/span[contains(@class, "data textscore textscore")]/text()').extract()
        #     item['date'] = site.select('div[@class="more_stats condensed_stats"]/ul/li/span[@class="data"]/text()').extract()
        #     items.append(item)
        # return items
              print(site.select('div[@class="basic_stat product_title"]/a/@href').extract())

