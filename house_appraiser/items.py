# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseAppraiserItem(scrapy.Item):
    # define the fields for your item here like:

    precio = scrapy.Field()
    superficie_total = scrapy.Field()
    superficie_cubierta = scrapy.Field()
    ambientes = scrapy.Field()
    baños = scrapy.Field()
    cocheras = scrapy.Field()
    dormitorios = scrapy.Field()
    toilettes = scrapy.Field()
    antiguedad = scrapy.Field()
    orientacion = scrapy.Field()
    estado = scrapy.Field()
    luminosidad = scrapy.Field()

    pass
