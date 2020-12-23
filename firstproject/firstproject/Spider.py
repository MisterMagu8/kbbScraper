

from scrapy import Spider, Request
from ..items import KbbItem
import re
class kbbSpider(Spider):
    #name: an attribute specifying a unique name to identify the spider
    name = "kbb_spider"
    
    #start_urls: an attribute listing the URLs the spider will start from
    allowed_domains = ['www.kbb.com']
    
    #allowed_urls: the main domain of the website you want to scrape
    start_urls = ['https://www.kbb.com/cars-for-sale/cars/used-cars/?p=1&color=']
    
    #parse(): a method of the spider responsible for processing a Response object downloaded from the URL and returning scraped data (as well as more URLs to follow, if necessary)
    
    def parse(self, response):
        text = response.xpath('//*[@id="listingsContainer"]//span[@class="page-numbers"]/text()').extract()[1]
        result_pages = ['https://www.kbb.com/cars-for-sale/cars/used-cars/?p={}&color={}'.format(x,y) for x in range(1, int(text)+1) for y in ['beige', 'black', 'blue', 'brown', 'burgundy','charcoal','gold','gray','green','offwhite','orange','pink','purple','red','silver','tan', 'turquoise','white','yellow']]
        for url in result_pages:
            yield Request(url=url, callback=self.parse_result_page)
    def parse_result_page(self, response):
        products = response.xpath('//*[@id="listingsContainer"]//a[@class="js-vehicle-name"]/@href').extract()
        product_urls = ['https://www.kbb.com' + x for x in products]
        for url in product_urls:
            yield Request(url=url, callback=self.parse_product_page)
    def parse_product_page(self, response):
        car = response.xpath('//*[@id="vehicleDetails"]/div/div/h1/text()').extract_first()
        price = response.xpath('//*[@id="pricingWrapper"]/span/span[@class ="price"]/text()').extract_first()
        mileage = response.xpath('//*[@id="keyDetailsContent"]/div/div/div/ul/li[@class="js-mileage"]/text()').extract_first()
        color = response.xpath('//*[@id="keyDetailsContent"]//li[contains(text(),"Exterior Color:")]/text()').extract_first()
        transmission = response.xpath('//*[@id="keyDetailsContent"]//li[contains(text(),"Transmission:")]/text()').extract_first()
        engine = response.xpath('//*[@id="keyDetailsContent"]//li[contains(text(),"Engine:")]/text()').extract_first()
        doors = response.xpath('//*[@id="keyDetailsContent"]//li[contains(text(),"Doors:")]/text()').extract_first()
        body = response.xpath('//*[@id="keyDetailsContent"]//li[contains(text(),"Body Style:")]/text()').extract_first()
        mpg = response.xpath('//*[@id="keyDetailsContent"]//li[contains(text(),"Fuel Economy:")]/text()').extract_first()
        drive_type = response.xpath('//*[@id="keyDetailsContent"]//li[contains(text(),"Drive Type:")]/text()').extract_first()
        kbb_expert_review = response.xpath('//*[@id="readExpertReview"]/p/span[@class="title-three"]/text()').extract_first()
        consumer_review = response.xpath('//*[@id="readConsumerReview"]/p/span[@class="title-three"]/text()').extract_first()
        location = response.xpath('//*[@id="aboutTheDealer"]//p/text()').extract()[:2]
        website = response.xpath('//*[@id="dealerDetailsModuleWebsite"]/@href').extract_first()
        item = KbbItem()
        item['body'] = body
        item['mpg'] = mpg
        item['kbb_expert_review'] = kbb_expert_review
        item['consumer_review'] = consumer_review
        item['car'] = car
        item['price'] = price
        item['mileage'] = mileage
        item['color'] = color
        item['transmission'] = transmission
        item['engine'] = engine
        item['doors'] = doors
        item['location'] = location
        item['website'] = website
        yield item