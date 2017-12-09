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

class hindinews(scrapy.Spider):
    name = "hindinews"

    domain = "https://navbharattimes.indiatimes.com"
    start_urls = ["https://navbharattimes.indiatimes.com"]
    store_id = []

    def __init__(self):
        self.verbs = open('hindiverb.csv', 'r')

    def start_requests(self):
       yield scrapy.Request(url=self.start_urls[0], callback=self.parse_store)

    # calculate number of pages
    def parse_store(self, response):
        try:
            headline = response.xpath(".//div[@class='mainarticle1']/h2//text()").extract_first().encode('utf8')
            category = self.filter_verb(headline)
            sub_headline_list = response.xpath(".//div[@class='other_main_news1']/ul/li")
            x = 1
            for news in sub_headline_list:
                item = ChainItem()
                      
                item['connector'] = x
                item['headline'] = headline
                item['category'] = category
                item['sub_headline'] = news.xpath('.//text()').extract_first()
                item['sub_category'] = self.filter_verb(news.xpath('.//text()').extract_first())

                x = x + 1
                yield item
                
        except:
            pdb.set_trace()
    
    def validate(self, value):
        if value != None:
            return value.strip().replace(u'\u2019', '-').replace('&#8217;', "'")
        else:
            return ""

    def filter_verb(self, article):
        for verb in self.verbs:
            article = article.replace(verb, '')

        return article




        

