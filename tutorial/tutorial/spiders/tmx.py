import scrapy


class QuotesSpider(scrapy.Spider):

    name = "TMX"

    def start_requests(self):
        url = 'https://web.tmxmoney.com/quote.php?qm_symbol=WEED&locale=EN'

        yield scrapy.Request(url=url, callback = self.parse)

    def parse(self, response):
        for quote in response.css('div.quote-wrapper'):
            yield{
                'price': quote.css('div.quote-rowd div.quote-price span.text::text').extract_first(),
            }
