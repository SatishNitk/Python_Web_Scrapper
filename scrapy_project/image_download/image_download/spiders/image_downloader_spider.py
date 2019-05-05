import scrapy
import logging

from image_download.items import ImageDownloadItem
class GoogleSpider(scrapy.Spider):
    name = 'google_logo'
    allowed_domains = ['google.com.au']
	
    start_urls = ['https://www.google.com.au']

    def parse(self, response):
        item = ImageDownloadItem()
        logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        item['image_urls'] = ["{}{}".format("https://www.google.com.au",response.xpath("//img[@id='hplogo']/@src").extract_first())]
        print("link ...............................{}".format(item))
        logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        return (item)