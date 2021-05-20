# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#
# import scrapy
#
#
# class DemoItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
import scrapy

class BookItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    publisher = scrapy.Field()
    price = scrapy.Field()
    detail = scrapy.Field()
