import scrapy
from file_download.items import FileDownloadItem

class Mp3downloader(scrapy.Spider):
	name ="downloader"
	start_urls = {
	"https://songspk3.org/student-of-the-year-2-songs.html"
	}

	def parse(self, response):
		k = 0 
		items = FileDownloadItem()
		for link in response.xpath("//div[contains(@id,'pi')]//following-sibling::ul//li//a"):
			url = link.xpath(".//@href").extract_first()
			self.logger.info("item= {}".format(url))
			items['file_urls'] = [url]  # it should be lust always...
			if(k==1):
				break
			k += 1
			yield (items)
