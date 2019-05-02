import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from brickset.items import BricksetItem

class BrickSetSpider(CrawlSpider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']
    custom_settings={ 'FEED_URI': "allset_%(time)s.json",
                       'FEED_FORMAT': 'json'}

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=['//li[@class="active"]','//li[@class="next"]']), callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        self.logger.info('Parse function called on %s', response.url)
        all_item = []
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            items = BricksetItem()

            NAME_SELECTOR = 'h1 ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
             
            items['name']= brickset.css(NAME_SELECTOR).extract_first(),
            items['pieces']= brickset.xpath(PIECES_SELECTOR).extract_first(),
            items['minifigs']= brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
            items['image']= brickset.css(IMAGE_SELECTOR).extract_first(),
            all_item.append(items)
        return (all_item)

        # NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        # if next_page:
        #     scrapy.Request(
        #         response.urljoin(next_page),
        #         callback=self.parse
        #     )
