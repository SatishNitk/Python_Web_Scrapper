# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline  #press control ad click on FilesPil=peline or get the code details..
from scrapy import Request

import logging

class FileDownloadNextPipeline(FilesPipeline):
	

	def get_media_requests(self, item, info):
		logging.warning("This is a warning")
		return [Request(x, meta = {'filename' : item.get('file_name')}) for x in item.get(self.files_urls_field, [])]


	def file_path(self, request, response=None, info=None):
		logging.warning("This is a warning secod ")
		url = request.url
		logging.warning(url)
		media_ext = os.path.splitext(url)[1]  # change to request.url after deprecation
		# logging.warning("hey warning",media_ext)
		# media_ext = ""
		return 'full/%s%s' % (request.meta['filename'], media_ext)

	
