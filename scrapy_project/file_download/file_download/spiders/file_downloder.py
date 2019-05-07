import scrapy
from file_download.items import FileDownloadItem

class Mp3downloader(scrapy.Spider):
	name ="downloader"
	start_urls = {
	"https://songspk3.org/student-of-the-year-2-songs.html"
	}

	def parse(self, response):
		print("parse.........................")
		items = FileDownloadItem()
		items['file_urls'] = []

		for link in response.xpath("//div[contains(@id,'pi')]//following-sibling::ul//li//a"):
			print("for loop.........................")
			items['file_urls'].append(link.xpath(".//@href").extract_first())
			items['name'] = link.xpath(".//text()").extract_first()
			self.logger.info(items['name'])	
			yield items
