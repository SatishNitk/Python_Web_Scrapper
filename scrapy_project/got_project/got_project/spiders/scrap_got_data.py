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
        # options.add_argument('-headless')
        driver = webdriver.Firefox(firefox_options=options)
        driver.get('https://www.washingtonpost.com/graphics/entertainment/game-of-thrones/?noredirect=on&utm_term=.047fbf407429#season-one')

        print("----------------------------------------------------------satish---------------------------")
        logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        season = response.xpath("//div[@id='season-one']//h3[@class='pg-h3 postoni']/text()").extract_first()
        death  = response.xpath("//h2[@id='season-death-counts-one']/text()").extract_first()
        # kk = driver.find_elements_by_xpath("//div[@id='season-one-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img")
        # print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",len(kk))
        # kk[0].click()
        # print("length1",len(driver.find_element_by_css_selector("div.modal-character-info").find_elements_by_tag_name("p")))
        # for pp in driver.find_element_by_css_selector("div.modal-character-info").find_elements_by_tag_name("p"):
        # 	print("valu-----------------",pp.text)



        # print("kkkllllllllllllll",driver.page_source)



        print("--------------------------------",season)
        print("--------------------------------",death)
        print("length",len(response.xpath("//div[@id='season-one-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img")))
        
        all_image = response.xpath("//div[@id='season-one-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image = [all_image[index] for index in range(len(all_image)) if index%2==0]
        # driver.close()
        # logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        start = 0
        for image in all_image:
        # image = all_image[0]
	        image_url = "https://www.washingtonpost.com/graphics/entertainment/game-of-thrones/" + str(image)
	        item['image_urls'] = [image_url]  # it should be list
	        kk = driver.find_elements_by_xpath("//div[@id='season-one-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img")
	        # print("kkkkkkww",kk)
	        kk[start].click()
	        all_value = []	
	        for pp in driver.find_element_by_css_selector("div.modal-character-info").find_elements_by_tag_name("p"):
	            # print("valu-----------------",pp.text)
	            all_value.append(pp.text)
	        item['Death'] = all_value[0]
	        item['Allegiance'] = all_value[1]
	        item['When'] = all_value[2]
	        item['Where'] = all_value[3]
	        item['Killer'] = all_value[4]
	        item['Method'] = all_value[5]
	        item['Method_category'] = all_value[6]
	        item['Reason'] = all_value[7]
	            
	        driver.find_element_by_xpath("//button[@class='back-button mb30']").click()
	        start +=3
	        print("allllllllllllllllllllllllllll",all_value)    
	        print("alllllllllllllllkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",item)   
	        all_value.clear()

        	yield item

#//div[@id='season-one-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img

