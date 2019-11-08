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
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//h3[@class="posting-title"]')),
             callback='parse_item', follow=False)
    }

    def parse_item(self, response):
        house = HouseAppraiserItem()

        items = response.xpath('/html/body/div[1]/main/div/div/article/div/section[1]/ul')

        for item in items:

            house['precio'] = item.xpath('/html/body/div[1]/main/div/div/aside/div/div[1]/div/div[1]/div[2]/span/text()').extract()

            for i in range(1, 12):

                label = item.xpath('li['+str(i)+']/span/text()').extract_first()

                if label == 'Superficie total':
                    house['superficie_total'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Superficie cubierta':
                    house['superficie_cubierta'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Ambientes':
                    house['ambientes'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Baños':
                    house['baños'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Cochera':
                    house['cocheras'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Dormitorios':
                    house['dormitorios'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Toilette':
                    house['toilettes'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Antigüedad':
                    house['antiguedad'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Orientación':
                    house['orientacion'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Estado del inmueble':
                    house['estado'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

                elif label == 'Luminosidad':
                    house['luminosidad'] = item.xpath('li['+str(i)+']/b/text()').extract_first()

        self.item_count += 1
        if self.item_count > 5000:
            raise CloseSpider('item_exceeded')
        yield house

