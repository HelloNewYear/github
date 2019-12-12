import scrapy
import re

class IMDB(scrapy.Spider):
    name = "imdb"
    start_urls = []
    for i in range(1,10):
        start_urls.append('http://www.imdb.cn/imdb250/'+str(i))

    def parse(self, response):
        movie_list = response.css('div.ss-3>a')
        for movie in movie_list:
            yield{
                'PosterURL': movie.css('div.hong>img::attr(src)').extract_first(),
                'Name': movie.css('div.honghe-3>p::text').extract_first(),
                'Score': movie.css('div.honghe-2>span>i::text').extract_first(),
                'Alias': movie.css('div.honghe-4>p>i::text').extract_first(),
                'EnglishName': movie.css('div.honghe-4>p::text').extract()[1][4:],
                'Director': movie.css('div.honghe-4>p>span::text').extract_first(),
                'Time': re.sub('<|>|/|i|p', '', movie.css('div.honghe-4>p').extract()[3]),
                'Synopsis': movie.css('div.honghe-5::text').extract_first(),
            }
