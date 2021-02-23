import scrapy

class LolSkin(scrapy.Spider):
    name = "lolskin"
    start_urls = ['https://lol.qq.com/data/info-heros.shtml']
    
    def parse(self, response):
        heros = response.css('.imgtextlist a::attr(href)').extract()
        for i in heros:
            yield scrapy.Request(url='https://lol.qq.com/data/'+i, callback=self.next_parse)

    def next_parse(self, response):
        img_list = response.css('#skinBG>li')
        for img in img_list:
            yield {
                'image_url': img.xpath('@src').extract_first(),
                'image_alt': img.xpath('@alt').extract_first(),
            }
