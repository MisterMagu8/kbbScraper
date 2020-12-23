

import scrapy
class KbbItem(scrapy.Item):
    car = scrapy.Field()
    mileage = scrapy.Field()
    price = scrapy.Field()
    color = scrapy.Field()
    transmission = scrapy.Field()
    engine = scrapy.Field()
    doors = scrapy.Field()
    body = scrapy.Field()
    mpg = scrapy.Field()
    kbb_expert_review = scrapy.Field()
    consumer_review = scrapy.Field()
    location = scrapy.Field()
    website = scrapy.Field()