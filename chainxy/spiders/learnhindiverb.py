import scrapy
import json
import re
import csv
import requests
from scrapy.spiders import Spider
from scrapy.http import FormRequest
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from chainxy.items import ChainItem

import pdb

class learnhindiverb(scrapy.Spider):
    name = "learnhindiverb"

    domain = "http://www.learning-hindi.com/post/1210783558/lesson-56-vocabulary-builder-verbs"
    start_urls = ["http://www.learning-hindi.com/post/1210783558/lesson-56-vocabulary-builder-verbs"]
    store_id = []

    def start_requests(self):
       yield scrapy.Request(url=self.start_urls[0], callback=self.parse_store)

    # calculate number of pages
    def parse_store(self, response):
        try:
            verb_list = response.xpath(".//div[contains(@class, 'caption clearfix rte')]/p")
            # pdb.set_trace()
            x = 0
            for i, verb in enumerate(verb_list):
                if self.validate(verb) == "":
                    continue
                item = ChainItem()
                x =  x + 1
                item['id'] = x
                item['verb'] = self.validate(verb)
                # pdb.set_trace()
                yield item
        except:
            pdb.set_trace()
    
    def validate(self, value):
        try:
            return value.xpath('.//big/big//text()').extract_first().strip().encode('utf8')
        except:
            return ""
        




        

