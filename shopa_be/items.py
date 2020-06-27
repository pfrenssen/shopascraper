import scrapy


# Model for a product.
class ProductItem(scrapy.Item):
    title = scrapy.Field()
    image = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()

    # Metadata
    url = scrapy.Field()
    retrieval_date = scrapy.Field()
    spider = scrapy.Field()
    project = scrapy.Field()
    instance = scrapy.Field()
