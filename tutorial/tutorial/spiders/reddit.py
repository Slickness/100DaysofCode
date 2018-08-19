import scrapy

class RedditbotSpider(scrapy.Spider):
    name =  "redditbot"

    def start_requests(self):
        allowed_domains = ['www.reddit.com/r/Daytrading/']
        start_urls = ['http://www.reddit.com/r/Daytrading/']

        yield  scrapy.Request(url = start_urls, callback = self.parse)

    def parse(self, response):
        titles = response.css('.s5kz2p-0::text').extract()
        yield(titles)


        for item in zip(titles):
            scraped_infor = {
                'title' : item[0],

            }

        yield scraped_info
