import scrapy
from file_download.items import FileDownloadItem
import os
class Mp3downloader(scrapy.Spider):
	name ="downloader"

	def get_url(self, film_name):
		print("get url starting----------------------")
		for i in range(0,len(film_name)):
			if(i%2==0):
				film_name.insert(i+1,"-")
		if(len(film_name)%2==0):
			film_name.insert(len(film_name)-1,"-")

		url_list = ["https://songspk3.org/"] + film_name + ["-songs.html"]
		return "".join(url_list)

	def __init__(self,*args, **kwargs):
		self.logger.info("init strting..........................")
		super(Mp3downloader, self).__init__(*args, **kwargs)
		endpoint = kwargs.get('film_name').split(" ")
		print("endpoint---------", endpoint)
		full_url = self.get_url(endpoint)
		self.start_urls = {
		full_url
		}


	def parse(self, response):
		print("parse.........................")
		items = FileDownloadItem()
		items['file_urls'] = []
		for link in response.xpath("//div[contains(@id,'pi')]//following-sibling::ul//li//a"):
			print("for loop.........................")
			extension = os.path.splitext(link.xpath(".//@href").extract_first())[1] #.mp3 .mp4
			if extension != ".zip":
				items['file_urls'].append(link.xpath(".//@href").extract_first())
			items['name'] = (link.xpath(".//text()").extract_first()).split("- ")[1]
			print("name-----------",items['name'])
			self.logger.info(items['name'])	
			yield items
		if not response.xpath("//div[contains(@id,'pi')]//following-sibling::ul//li//a"):
			print("HEY PLEASE ENTER VALID MOVIES NAME.....................")

#to run
#scrapy crawl downloader -a film_name="Student Of The Year 2"