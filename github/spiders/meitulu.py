import scrapy

class Meitulu(scrapy.Spider):
    name = "meitulu"
    start_urls = ['https://www.meitulu.com/item/12410.html']

    def parse(self, response):
        img_list = response.css('div.content center img')
        for img in img_list:
            yield {
                'image_url': img.xpath('@src').extract_first(),
                'image_alt': img.xpath('@alt').extract_first(),
            }
        next_page = 'https://www.meitulu.com' + response.css('body>center span+a').xpath('@href').extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
