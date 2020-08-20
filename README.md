### Downloading and processing files and images
#### https://doc.scrapy.org/en/latest/topics/media-pipeline.html
#### https://support.scrapinghub.com/support/solutions/articles/22000200389-images-storage-addon
---

`meitulu.py`

    import scrapy
    from instagram.items import InstagramItem

    class Meitulu(scrapy.Spider):
        name = "meitulu"
        start_urls = ['http://www.520mojing.com/']

        def parse(self, response):
            img_urls = ['http://img.520mojing.com/data/attachment/forum/201806/15/072326uzya74dqr45ba61q.jpg']
            for img in img_urls:
                item = InstagramItem()
                item['url'] = img
                yield item

---

`items.py`

    import scrapy

    class InstagramItem(scrapy.Item):
        url = scrapy.Field()

---

`pipelines.py`

    import scrapy
    from scrapy.pipelines.images import ImagesPipeline

    class InstagramPipeline(ImagesPipeline):
        def get_media_requests(self, item, info):
            yield scrapy.Request(item['url'])
 
 ---
 
 `settings.py`
 
    # Configure item pipelines
    # See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
    #ITEM_PIPELINES = {
    #    'instagram.pipelines.InstagramPipeline': 300,
    #}
    ITEM_PIPELINES = {'instagram.pipelines.InstagramPipeline': 1}
    IMAGES_STORE = '/root/pic'
