import scrapy
from scrapy.loader.processors import TakeFirst


# Model for a product.
class ProductItem(scrapy.Item):
    title = scrapy.Field(output_processor=TakeFirst())
    image = scrapy.Field(output_processor=TakeFirst())
    category = scrapy.Field()
    price = scrapy.Field(output_processor=TakeFirst())
    description = scrapy.Field(output_processor=TakeFirst())

    # Metadata
    url = scrapy.Field(output_processor=TakeFirst())
    retrieval_date = scrapy.Field(output_processor=TakeFirst())
    spider = scrapy.Field(output_processor=TakeFirst())
    project = scrapy.Field(output_processor=TakeFirst())
    instance = scrapy.Field(output_processor=TakeFirst())
