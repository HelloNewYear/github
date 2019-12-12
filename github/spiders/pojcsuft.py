import scrapy

class Pojcsuft(scrapy.Spider):
    name = "pojcsuft"
    start_urls = ['http://poj.org/searchuser?key=csuft&field=school&B1=GO']

    def parse(self, response):
        tr_list = response.css('center tr')
        for tr in tr_list[1:]:
            td = tr.css('td::text').extract()
            yield{
                'No.': td[0],
                'User': tr.css('td')[1].css('a::text').extract_first(),
                'Nick Name': td[1],
                'School': td[2],
                'Email': td[3],
                'Solved': td[4],
                'Submissions': td[5],
            }
