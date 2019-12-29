import scrapy
import re
import requests
import redis

class Proxy(scrapy.Spider):
    name = "proxy"
    start_urls = ['http://icanhazip.com/',]

    def parse(self, response):
        yield {
          'IP': response.text,
        }
