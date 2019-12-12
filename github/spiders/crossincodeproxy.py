import scrapy

class Crossincodeproxy(scrapy.Spider):
    name = "crossincodeproxy"
    start_urls = ['http://lab.crossincode.com/proxy/']

    def parse(self, response):
        tr_list = response.css('table tr')[1:]
        for tr in tr_list:
            trc = tr.css('td::text').extract()
            yield {
                'IP': trc[0],
                'Port': trc[1],
                'Degree_of_anonymity': trc[2],
                'Type': trc[3],
                'Location': trc[4],
                'Final_verification_time': trc[5],
            }
