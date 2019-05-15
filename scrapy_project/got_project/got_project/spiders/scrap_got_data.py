import scrapy
import logging
from selenium import webdriver
from got_project.items import GotProjectItem
class GoogleSpider(scrapy.Spider):
    name = 'google_logo'
    allowed_domains = ['www.washingtonpost.com']

	
    start_urls = ['https://www.washingtonpost.com/graphics/entertainment/game-of-thrones/?noredirect=on&utm_term=.df4ec9592e08#season-two']

    def parse(self, response):
        item = GotProjectItem()
        options = webdriver.FirefoxOptions()
        # options.add_argument('-headless')
        driver = webdriver.Firefox(firefox_options=options)
        # driver.get('https://www.washingtonpost.com/graphics/entertainment/game-of-thrones/?noredirect=on&utm_term=.047fbf407429#season-one')
        driver.get(response.url)
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

        start = 0
        print("--------------------------------",season)
        print("--------------------------------",death)
        print("length",len(response.xpath("//div[@id='season-one-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img")))
        

        all_image = []
        #             ---- season 1----------
        all_image_first_level = response.xpath("//div[@id='season-one-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_first_level = [all_image_first_level[index] for index in range(len(all_image_first_level)) if index%2==0]
        
        all_image = all_image_first_level

        print("all-image length.",len(all_image))
# second block image----------
        all_image_second_level = response.xpath("//div[@id='season-one-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_second_level = [all_image_second_level[index] for index in range(len(all_image_second_level)) if index%2==0]
        print("length of all_imagesecond lebel",len(all_image_second_level))
        
        all_image += all_image_second_level
        print("length of all_image",len(all_image))
        print("--------------------------",len(all_image_second_level))

#third block image
        all_image_third_level_s1 = response.xpath("//div[@id='season-one-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image += all_image_third_level_s1


        # season-----------2 

        all_image_first_level = response.xpath("//div[@id='season-two-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_first_level = [all_image_first_level[index] for index in range(len(all_image_first_level)) if index%2==0]
        
        all_image += all_image_first_level
        
        # logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        print("all-image length.",len(all_image))
# second block image----------
        all_image_second_level = response.xpath("//div[@id='season-two-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_second_level = [all_image_second_level[index] for index in range(len(all_image_second_level)) if index%2==0]
        print("length of all_imagesecond lebel",len(all_image_second_level))
        
        all_image += all_image_second_level
        print("length of all_image",len(all_image))
        print("--------------------------",len(all_image_second_level))
#third block image
        all_image_third_level_s1 = response.xpath("//div[@id='season-two-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image += all_image_third_level_s1

        # season-----------3

        all_image_first_level = response.xpath("//div[@id='season-three-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_first_level = [all_image_first_level[index] for index in range(len(all_image_first_level)) if index%2==0]
        
        all_image += all_image_first_level
        
        # logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        print("all-image length.",len(all_image))
# second block image----------
        all_image_second_level = response.xpath("//div[@id='season-three-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_second_level = [all_image_second_level[index] for index in range(len(all_image_second_level)) if index%2==0]
        print("length of all_imagesecond lebel",len(all_image_second_level))
        
        all_image += all_image_second_level
        print("length of all_image",len(all_image))
        print("--------------------------",len(all_image_second_level))
#third block image
        all_image_third_level_s1 = response.xpath("//div[@id='season-three-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image += all_image_third_level_s1
         
         # season-----------4

        all_image_first_level = response.xpath("//div[@id='season-four-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_first_level = [all_image_first_level[index] for index in range(len(all_image_first_level)) if index%2==0]
        
        all_image += all_image_first_level
        # logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        print("all-image length.",len(all_image))
# second block image----------
        all_image_second_level = response.xpath("//div[@id='season-four-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_second_level = [all_image_second_level[index] for index in range(len(all_image_second_level)) if index%2==0]
        print("length of all_imagesecond lebel",len(all_image_second_level))
        
        all_image += all_image_second_level
        print("length of all_image",len(all_image))
        print("--------------------------",len(all_image_second_level))

#third block image
        all_image_third_level_s1 = response.xpath("//div[@id='season-four-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image += all_image_third_level_s1

          # season-----------5

        all_image_first_level = response.xpath("//div[@id='season-five-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_first_level = [all_image_first_level[index] for index in range(len(all_image_first_level)) if index%2==0]
        
        all_image += all_image_first_level
        
        # logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        print("all-image length.",len(all_image))
# second block image----------
        all_image_second_level = response.xpath("//div[@id='season-five-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_second_level = [all_image_second_level[index] for index in range(len(all_image_second_level)) if index%2==0]
        print("length of all_imagesecond lebel",len(all_image_second_level))
        
        all_image += all_image_second_level
        print("length of all_image",len(all_image))
        print("--------------------------",len(all_image_second_level))
#third block image
        all_image_third_level_s1 = response.xpath("//div[@id='season-five-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image += all_image_third_level_s1
         
          # season-----------6

        all_image_first_level = response.xpath("//div[@id='season-six-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_first_level = [all_image_first_level[index] for index in range(len(all_image_first_level)) if index%2==0]
        
        all_image += all_image_first_level
        
        # logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        print("all-image length.",len(all_image))
# second block image----------
        all_image_second_level = response.xpath("//div[@id='season-six-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_second_level = [all_image_second_level[index] for index in range(len(all_image_second_level)) if index%2==0]
        print("length of all_imagesecond lebel",len(all_image_second_level))
        
        all_image += all_image_second_level
        print("length of all_image",len(all_image))
        print("--------------------------",len(all_image_second_level))

#third block image
        all_image_third_level_s1 = response.xpath("//div[@id='season-six-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image += all_image_third_level_s1

          # season-----------7

        all_image_first_level = response.xpath("//div[@id='season-seven-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_first_level = [all_image_first_level[index] for index in range(len(all_image_first_level)) if index%2==0]
        
        all_image += all_image_first_level
        
        # logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        print("all-image length.",len(all_image))
# second block image----------
        all_image_second_level = response.xpath("//div[@id='season-seven-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_second_level = [all_image_second_level[index] for index in range(len(all_image_second_level)) if index%2==0]
        print("length of all_imagesecond lebel",len(all_image_second_level))
        
        all_image += all_image_second_level
        print("length of all_image",len(all_image))
        print("--------------------------",len(all_image_second_level))

#third block image
        all_image_third_level_s1 = response.xpath("//div[@id='season-seven-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image += all_image_third_level_s1

          # season-----------8

        all_image_first_level = response.xpath("//div[@id='season-eight-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_first_level = [all_image_first_level[index] for index in range(len(all_image_first_level)) if index%2==0]
        
        all_image += all_image_first_level
        
        # logging.log(logging.WARNING, "This is a warning: opening------------------------------------------------------")
        print("all-image length.",len(all_image))
# second block image----------
        all_image_second_level = response.xpath("//div[@id='season-eight-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image_second_level = [all_image_second_level[index] for index in range(len(all_image_second_level)) if index%2==0]
        print("length of all_imagesecond lebel",len(all_image_second_level))
        
        all_image += all_image_second_level
        print("length of all_image",len(all_image))
        print("--------------------------",len(all_image_second_level))
#third block image
        all_image_third_level_s1 = response.xpath("//div[@id='season-eight-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img/@data-src").extract()
        all_image += all_image_third_level_s1



        #  ------------ for click on image  season --1 ------------
        all_image_click = []
        img_click_first_level = driver.find_elements_by_xpath("//div[@id='season-one-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_first_level = [img_click_first_level[index] for index in range(len(img_click_first_level)) if index%3==0]
        img_click_second_level = driver.find_elements_by_xpath("//div[@id='season-one-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_second_level = [img_click_second_level[index] for index in range(len(img_click_second_level)) if index%3==0]
        img_click_third_level = driver.find_elements_by_xpath("//div[@id='season-one-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img")


        
        all_image_click +=  img_click_first_level + img_click_second_level + img_click_third_level
        #  ------------ for click on image  season --2 ------------
        img_click_first_level = driver.find_elements_by_xpath("//div[@id='season-two-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_first_level = [img_click_first_level[index] for index in range(len(img_click_first_level)) if index%3==0]
        img_click_second_level = driver.find_elements_by_xpath("//div[@id='season-two-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_second_level = [img_click_second_level[index] for index in range(len(img_click_second_level)) if index%3==0]
        img_click_third_level = driver.find_elements_by_xpath("//div[@id='season-two-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img")
        

        all_image_click +=  img_click_first_level + img_click_second_level + img_click_third_level
         #  ------------ for click on image  season --3 ------------
        img_click_first_level = driver.find_elements_by_xpath("//div[@id='season-three-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_first_level = [img_click_first_level[index] for index in range(len(img_click_first_level)) if index%3==0]
        img_click_second_level = driver.find_elements_by_xpath("//div[@id='season-three-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_second_level = [img_click_second_level[index] for index in range(len(img_click_second_level)) if index%3==0]
        
        img_click_third_level = driver.find_elements_by_xpath("//div[@id='season-third-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img")
        all_image_click +=  img_click_first_level + img_click_second_level + img_click_third_level

         #  ------------ for click on image  season --4------------
        img_click_first_level = driver.find_elements_by_xpath("//div[@id='season-four-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_first_level = [img_click_first_level[index] for index in range(len(img_click_first_level)) if index%3==0]
        img_click_second_level = driver.find_elements_by_xpath("//div[@id='season-four-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_second_level = [img_click_second_level[index] for index in range(len(img_click_second_level)) if index%3==0]
        img_click_third_level = driver.find_elements_by_xpath("//div[@id='season-four-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img")
        all_image_click +=  img_click_first_level + img_click_second_level + img_click_third_level

         #  ------------ for click on image  season --5 ------------
        img_click_first_level = driver.find_elements_by_xpath("//div[@id='season-five-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_first_level = [img_click_first_level[index] for index in range(len(img_click_first_level)) if index%3==0]
        img_click_second_level = driver.find_elements_by_xpath("//div[@id='season-five-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_second_level = [img_click_second_level[index] for index in range(len(img_click_second_level)) if index%3==0]
        img_click_third_level = driver.find_elements_by_xpath("//div[@id='season-five-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img")
        all_image_click +=  img_click_first_level + img_click_second_level + img_click_third_level

           #  ------------ for click on image  season --6 ------------
        img_click_first_level = driver.find_elements_by_xpath("//div[@id='season-six-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_first_level = [img_click_first_level[index] for index in range(len(img_click_first_level)) if index%3==0]
        img_click_second_level = driver.find_elements_by_xpath("//div[@id='season-six-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_second_level = [img_click_second_level[index] for index in range(len(img_click_second_level)) if index%3==0]
        img_click_third_level = driver.find_elements_by_xpath("//div[@id='season-six-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img")
        all_image_click +=  img_click_first_level + img_click_second_level + img_click_third_level

   #  ------------ for click on image  season --7 ------------
        img_click_first_level = driver.find_elements_by_xpath("//div[@id='season-seven-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_first_level = [img_click_first_level[index] for index in range(len(img_click_first_level)) if index%3==0]
        img_click_second_level = driver.find_elements_by_xpath("//div[@id='season-seven-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_second_level = [img_click_second_level[index] for index in range(len(img_click_second_level)) if index%3==0]
        img_click_third_level = driver.find_elements_by_xpath("//div[@id='season-seven-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img")
        all_image_click +=  img_click_first_level + img_click_second_level + img_click_third_level

   #  ------------ for click on image  season --8 ------------
        img_click_first_level = driver.find_elements_by_xpath("//div[@id='season-eight-inner']//div[@class='level-wrapper level-four-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_first_level = [img_click_first_level[index] for index in range(len(img_click_first_level)) if index%3==0]
        img_click_second_level = driver.find_elements_by_xpath("//div[@id='season-eight-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img")
        img_click_second_level = [img_click_second_level[index] for index in range(len(img_click_second_level)) if index%3==0]
        img_click_third_level = driver.find_elements_by_xpath("//div[@id='season-eight-inner']//div[@class='level-wrapper level-two-wrapper']//div[@class='img-info-wrapper']//img")
        all_image_click +=  img_click_first_level + img_click_second_level + img_click_third_level


        
        print("length of all image----------------------------",len(all_image_click))
        print("length of all imagkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkke----------------------------",all_image_click)


        for image in all_image:
        # image = all_image[0]
	        image_url = "https://www.washingtonpost.com/graphics/entertainment/game-of-thrones/" + str(image)
	        item['image_urls'] = [image_url]  # it should be list
	        # print("kkkkkkww",kk)
	        all_image_click[start].click()
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
	        start +=1
	        print("allllllllllllllllllllllllllll",all_value)    
	        print("alllllllllllllllkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",item)   
	        all_value.clear()

        	yield item

        driver.close()

        # next_page_url = "https://www.washingtonpost.com/graphics/entertainment/game-of-thrones/?noredirect=on&utm_term=.81cb55368531#season-two"
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))



    

#//div[@id='season-one-inner']//div[@class='level-wrapper level-three-wrapper']//div[@class='img-info-wrapper']//img

