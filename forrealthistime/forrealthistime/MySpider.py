
import Scrapy

class MySpider(scrapy.spider):
    name = 'spood'
    start_urls = ['https://www.kbb.com/cars-for-sale/cars/used-cars/?p=1&color=']

    def parse(self, response):
        print(response)
        next_page = response.css('li.next a::attr("href")').get()

        if next_page is not None:
            yield response.follow(next_page, self.parse)