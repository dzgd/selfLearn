# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# import scrapy
#
#
# class PopulationInfoItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

import scrapy

class populationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id=scrapy.Field()
    code=scrapy.Field()
    name=scrapy.Field()
    relation=scrapy.Field()
    shenfenzhenghaoma=scrapy.Field()
