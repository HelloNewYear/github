import scrapy

class Xiameijiang(scrapy.Spider):
    name = "xiameijiang"
    start_urls = ['http://www.cct58.com/mneinv/36597/mx27/']

    def parse(self, response):
        xurls = response.css('div[id=my-yy] a::attr(href)').extract()
        for x in xurls:
            yield scrapy.Request(url=x, callback=self.next_parse)

    def next_parse(self, response):
        yurls = response.css('div[class=my-mx-top10] a::attr(href)').extract()
        for y in yurls:
            yield scrapy.Request(url=y, callback=self.third_parse)

    def third_parse(self, response):
        z = response.css('div[id=confontz] img::attr(src)').extract_first()
        yield {
            'img_url': z,
        }
