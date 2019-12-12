import scrapy

class Wenzhi(scrapy.Spider):
    name = "wenzhi"
    url = 'http://81rc.81.cn/news/2019-09/09/content_9615876.htm'
    page = 97
    start_urls = [url]
    for i in range(2,page+1):
        start_urls.append(url[:-4]+'_'+str(i)+'.htm')

    def parse(self, response):
        picture_url = response.css('#Zoom>center>img::attr(src)').extract()
        yield {
            'picture_url': picture_url,
        }
