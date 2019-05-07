# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import random
from scrapy import Request
import os

from scrapy.pipelines.images import FilesPipeline

class FileDownloadPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        print("file_path.........................")
        if not isinstance(request, Request):
            url = request
        else:
            url = request.url
        media_guid = "saish" + str(random.randrange(20, 50, 3)) # change to request.url after deprecation
        media_ext =os.path.splitext(url)[1]  # change to request.url after deprecation
        return 'mp3_folder/%s%s' % (request.meta['filename'], media_ext)

    def get_media_requests(self, item, info):
        print("get_media_requests.........................")

        kk =  [Request(x, meta = {'filename' : item['name']}) for x in item.get(self.files_urls_field, [])]
        return kk
