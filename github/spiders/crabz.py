import scrapy
import re

class Crabz(scrapy.Spider):
    name = "crabz"
    start_urls = ['http://www.itsec.gov.cn/ryzc/rcpgg/index.html']
    for i in range(1,11):
        start_urls.append('http://www.itsec.gov.cn/ryzc/rcpgg/index_{}.html'.format(i))

    def parse(self, response):
        url_list = response.css('div.list-every li a::attr(href)').extract()
        for u in url_list:
            url = response.urljoin('http://www.itsec.gov.cn/ryzc/rcpgg'+u[1:])
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        tables = response.css('table')
        for table in tables:
            trs = table.css('tr')[1:]
            for tr in trs:
                s0 = tr.extract().replace('\n', '').replace(' ', '')
                s1 = re.sub(r'<.+?>', ',', s0).strip(',')
                s2 = re.sub(r',+', ',', s1)
                yield {
                    'info': s2,
                }
