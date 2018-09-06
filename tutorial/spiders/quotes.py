# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        qutoes = response.css('.quote')
        for qutoe in qutoes:
            item = TutorialItem()
            item['text'] = qutoe.css('.text::text').extract_first()
            item['author'] = qutoe.css('.author::text').extract_first()
            item['tags'] = qutoe.css('.tags .tag::text').extract()
            yield item

        next=response.css('.pager .next a::attr("href")').extract_first()
        url=response.urljoin(next)
        yield scrapy.Request(url=url,callback=self.parse)
