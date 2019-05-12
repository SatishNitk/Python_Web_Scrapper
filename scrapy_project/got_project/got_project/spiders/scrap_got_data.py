import scrapy
import logging
from selenium import webdriver
from got_project.items import GotProjectItem
class GoogleSpider(scrapy.Spider):
    name = 'google_logo'
    allowed_domains = ['www.washingtonpost.com']

	
    start_urls = ['https://www.washingtonpost.com/graphics/entertainment/game-of-thrones/?noredirect=on&utm_term=.047fbf407429#season-one']

    def parse(self, response):
        item = GotProjectItem()
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(firefox_options=options)
        driver.get('https://stackoverflow.com/questions/38521864/click-button-on-website-using-scrapy?rq=1')

        print("----------------------------------------------------------satish---------------------------")
        logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        season = response.xpath("//div[@id='season-one']//h3[@class='pg-h3 postoni']/text()").extract_first()
        death  = response.xpath("//h2[@id='season-death-counts-one']/text()").extract_first()
        
        print("--------------------------------",season)
        print("--------------------------------",death)
        print("length",len(response.xpath("//div[@id='season-one-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img")))
        
        all_image = response.xpath("//div[@id='season-one-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image = [all_image[index] for index in range(len(all_image)) if index%2==0]
        # logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        for image in all_image:
        	image_url = "https://www.washingtonpost.com/graphics/entertainment/game-of-thrones/" + str(image)
        	item['image_urls'] = [image_url]  # it should be list
        	# item['name'] =
        	yield item



