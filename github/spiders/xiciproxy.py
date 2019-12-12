import scrapy
import re

class XiciProxy(scrapy.Spider):
    name = "xiciproxy"
    start_urls = ['https://www.xicidaili.com/nn/',
                  'https://www.xicidaili.com/nt/',
                  'https://www.xicidaili.com/wn/',
                  'https://www.xicidaili.com/wt/',]

    def parse(self, response):
        pattern = re.compile(r'<.+?>')
        tr_list = response.css('tr[class]')
        for tr in tr_list:
            td = tr.css('td').extract()
            yield {
                'IP': re.sub(pattern, '', td[1]),
                'Port': re.sub(pattern, '', td[2]),
                'Location': re.sub(pattern, '', td[3]).replace(' ', '').replace('\n', ''),
                'Degree_of_anonymity': re.sub(pattern, '', td[4]),
                'Protocol': re.sub(pattern, '', td[5]),
                'TTL': re.sub(pattern, '', td[8]),
                'Final_verification_time': re.sub(pattern, '', td[9]),
            }
        '''
        next_page = 'http://www.xicidaili.com' + response.css('div.pagination>a.next_page::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        '''
