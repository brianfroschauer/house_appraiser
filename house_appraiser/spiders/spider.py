from scrapy.exceptions import CloseSpider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from house_appraiser.items import HouseAppraiserItem


class HouseAppraiserSpider(CrawlSpider):

    name = 'house_appraiser'
    item_count = 0
    allowed_domain = ['https://www.zonaprop.com.ar']
    start_urls = ['https://www.zonaprop.com.ar/departamentos-venta-pagina-1.html']
    rules = {
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//li[@class="pag-go-next"]/a'))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//h3[@class="posting-title"]')),
             callback='parse_item', follow=False)
    }

    def parse_item(self, response):
        item = HouseAppraiserItem()

        item['titulo'] = response.xpath('normalize-space(//div[@class="section-title"]/h1)').extract()
        item['precio'] = response.xpath('normalize-space(//*[@id="sidebar-price-container"]/div/div[1]/div[2])').extract()
        item['superficie_total'] = response.xpath('normalize-space(//*[@id="article-container"]/section[1]/ul/li[1]/b)').extract()
        item['superficie_cubierta'] = response.xpath('normalize-space(//*[@id="article-container"]/section[1]/ul/li[2]/b)').extract()
        item['ambientes'] = response.xpath('normalize-space(//*[@id="article-container"]/section[1]/ul/li[3]/b)').extract()
        item['baños'] = response.xpath('normalize-space(//*[@id="article-container"]/section[1]/ul/li[4]/b)').extract()
        item['cocheras'] = response.xpath('normalize-space(//*[@id="article-container"]/section[1]/ul/li[5]/b)').extract()
        item['dormitorios'] = response.xpath('normalize-space(//*[@id="article-container"]/section[1]/ul/li[6]/b)').extract()
        item['toilettes'] = response.xpath('normalize-space(//*[@id="article-container"]/section[1]/ul/li[7]/b)').extract()
        item['antiguedad'] = response.xpath('normalize-space(//*[@id="article-container"]/section[1]/ul/li[8]/b)').extract()
        item['disposicion'] = response.xpath('normalize-space(//*[@id="article-container"]/section[1]/ul/li[9]/b)').extract()
        item['orientacion'] = response.xpath('normalize-space(//*[@id="article-container"]/section[1]/ul/li[10]/b)').extract()
        item['estado'] = response.xpath('normalize-space(//*[@id="article-container"]/section[1]/ul/li[11]/b)').extract()
        item['luminosidad'] = response.xpath('normalize-space(//*[@id="article-container"]/section[1]/ul/li[12]/b)').extract()

        self.item_count += 1
        if self.item_count > 2:
            raise CloseSpider('item_exceeded')
        yield item

