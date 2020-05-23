from scrapy.exceptions import CloseSpider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from house_appraiser.items import HouseAppraiserItem


class HouseAppraiserSpider(CrawlSpider):

    name = 'house_appraiser'
    item_count = 0
    allowed_domain = ['https://www.zonaprop.com.ar']
    start_urls = ['https://www.zonaprop.com.ar/casas-venta.html']
    rules = {
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//li[@class="pag-go-next"]/a'))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//h2[@class="posting-title"]')),
             callback='parse_item', follow=False)
    }

    def parse_item(self, response):
        house = HouseAppraiserItem()

        items = response.xpath('/html/body/div[2]/main/div/div/article/div/section[1]/ul')

        for item in items:
            house['price'] = item.xpath('/html/body/div[2]/main/div/div/aside/div/div[1]/div/div[1]/div[2]/span/text()').extract()

            for i in range(1, 12):

                label = item.xpath('li['+str(i)+']/span/text()').extract_first()

                if label == 'Superficie total':
                    house['total_surface'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Superficie cubierta':
                    house['covered_surface'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Ambientes':
                    house['rooms'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Baños':
                    house['bathrooms'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Cochera':
                    house['garages'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Dormitorios':
                    house['bedrooms'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Toilette':
                    house['toilettes'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Antigüedad':
                    house['antiquity'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                house['zone'] = item.xpath(
                    '/html/body/div[2]/main/div/div/article/div/hgroup/h2[2]/span/text()'
                ).extract_first()

        self.item_count += 1
        if self.item_count > 10000:
            raise CloseSpider('item_exceeded')
        yield house

