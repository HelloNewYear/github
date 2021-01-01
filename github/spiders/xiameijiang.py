import scrapy
import re

class Xiameijiang(scrapy.Spider):
    name = "xiameijiang"
    start_urls = ['https://www.cct58.com/mneinv/36597/mx27id8347pg0.html']

    def parse(self, response):
        us = response.css('div.cm a::attr(href)').extract()
        pg = response.css('div.cm .t').extract()
        
        xurls = []
        for i in range(15):
            pm = int(re.search(r'\d+', pg[i]).group())
            for j in range(pm):
                xurls.append(us[i][:-6] + str(j) + '.html')
        
        for x in xurls:
            yield scrapy.Request(url=x, callback=self.next_parse)

    def next_parse(self, response):
        z = response.css('#confontz img::attr(src)').extract_first()
        yield {
            'img_url': z,
        }
