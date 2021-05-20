# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#
# import scrapy
#
#
# class Share01Item(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
import scrapy

class lineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id=scrapy.Field()
    name=scrapy.Field()
    new_price=scrapy.Field()
    up_rate=scrapy.Field()
    down_rate=scrapy.Field()
    pass_number=scrapy.Field()
    pass_money=scrapy.Field()
    rate=scrapy.Field()
    highest=scrapy.Field()
    lowest=scrapy.Field()
    today=scrapy.Field()
    yesterday=scrapy.Field()

