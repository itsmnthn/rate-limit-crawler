import scrapy


class AttackSpider(scrapy.Spider):
    name = 'attack'
    start_urls = []
    custom_settings = {
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
    }

    def __init__(self, url='', rq='2000', **kwargs):
        self.start_urls = [url] * int(rq)  # py36
        super().__init__(**kwargs)  # python3

    def parse(self, response):
        print('response: ', response)
