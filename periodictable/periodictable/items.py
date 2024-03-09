# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst


class PeriodictableItem(scrapy.Item):
    # define the fields for your item here like:
    column = scrapy.Field(
        output_processor = TakeFirst()
    )

    row = scrapy.Field(
        output_processor=TakeFirst()
    )

