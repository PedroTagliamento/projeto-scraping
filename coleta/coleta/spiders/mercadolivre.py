import scrapy

class MercadoLivreSpider(scrapy.Spider):
    name = "mercadolivre"
    start_urls = ['https://lista.mercadolivre.com.br/tenis-corrida-masculino']

    def parse(self, response):
          
        # Seu código de parsing aqui
        products = response.css('div.ui-search-result__content')

        for product in products: 
           yield {
               'brand' : product.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get()
           }
