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

class hindiverb(scrapy.Spider):
    name = "hindiverb"

    domain = "http://mylanguages.org/hindi_verbs.php"
    start_urls = ["http://mylanguages.org/hindi_verbs.php"]
    store_id = []

    def start_requests(self):
       yield scrapy.Request(url=self.start_urls[0], callback=self.parse_store)

    # calculate number of pages
    def parse_store(self, response):
        try:
            verb_list = response.xpath(".//table[@id='example2']/tbody/tr")
            # pdb.set_trace()
            x = 0
            value = ''
            for verb in verb_list:
                if self.validate(verb) == "":
                    continue
                value = value + self.validate(verb) 
                
                # pdb.set_trace()
            value = value.replace('|', '');
            value_list = value.split();
            x = 1
            for val in value_list:
                if val == "":
                    continue

                item = ChainItem()
                item['id'] = x;
                item['verb'] = val.strip().encode('utf8')

                x = x + 1;
                yield item

        except:
            pdb.set_trace()
    
    def validate(self, value):
        try:
            return value.xpath('.//td[2]/b//text()').extract_first().strip()
        except:
            return ""
        




        

