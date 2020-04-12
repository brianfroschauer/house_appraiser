# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseAppraiserItem(scrapy.Item):
    # define the fields for your item here like:

    price = scrapy.Field()
    total_surface = scrapy.Field()
    covered_surface = scrapy.Field()
    rooms = scrapy.Field()
    bathrooms = scrapy.Field()
    garages = scrapy.Field()
    bedrooms = scrapy.Field()
    toilettes = scrapy.Field()
    antiquity = scrapy.Field()
    zone = scrapy.Field()

    pass
