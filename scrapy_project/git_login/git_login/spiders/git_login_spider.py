from scrapy.item import Item, Field
from scrapy.http import FormRequest
import scrapy
from scrapy.utils.response import open_in_browser


class GitSpider(scrapy.Spider):
    name = "github"
    allowed_domains = ["github.com"]
    start_urls = ["https://www.github.com/login"]

    def parse(self, response):
        formdata = {'login': 'satishoc',
                'password': 'guptakumar1234' }
        yield FormRequest.from_response(response,
                                        formdata=formdata,
                                        clickdata={'name': 'commit'},
                                        callback=self.parse1)

    def parse1(self, response):
        print("okkkkkkkkkkkkkkkkkkkkkkk")
        self.logger.info("sss")
        open_in_browser(response)
