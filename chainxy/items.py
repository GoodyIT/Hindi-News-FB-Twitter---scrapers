# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ChainItem(Item):
	id = Field()
	connector = Field()
	category = Field()
	verb = Field()
	consonant = Field()
	headline = Field()
	sub_headline = Field()
	sub_category = Field()
    
    
    