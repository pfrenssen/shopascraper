import datetime
import json
import re
import socket

from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from shopa_be.items import ProductItem


class ProductSpider(CrawlSpider):
    name = 'products'
    allowed_domains = ['shopa.be']

    rules = (
        Rule(LinkExtractor(allow=r'^https://www.shopa.be/product/'), callback='parse_item', follow=False),
    )

    def __init__(self, partner=None, *args, **kwargs):
        print(partner)
        super(ProductSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.shopa.be/partner/%s' % partner]

    def parse_item(self, response):
        l = ItemLoader(item=ProductItem(), response=response)
        l.add_xpath('title', '//div[contains(@class, "product-info")]/h1/text()')
        l.add_xpath('image', '//section[@id="product-slider"]//div[contains(@class, "active")]/img/@src')
        l.add_xpath('category', '//section[contains(@class, "breadcrumbs")]//ul//a/text()')
        l.add_xpath('price', '//section[@class="product-pricing"]//span[contains(concat(" ", @class, " "), " product-price ")]/text()')
        l.add_xpath('description', '//section[@class="product-description"]/div[contains(@class, "description_product")]')

        l.add_value('url', response.url)
        l.add_value('retrieval_date', datetime.datetime.now())
        l.add_value('spider', self.name)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('instance', socket.gethostname())

        return l.load_item()
