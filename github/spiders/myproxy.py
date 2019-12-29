import scrapy
import re
import requests
import redis

class Myproxy(scrapy.Spider):
    name = "myproxy"
    start_urls = ['http://icanhazip.com/',]

    def parse(self, response):
        yield {
          'IP': response.text,
        }
