# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:32:11 2017
This example shows fundamentals of HTML, CSS, Python, Scrapy, and Javascript
@author: Nelson Stacy
"""
import scrapy

class JobsSpider(scrapy.Spider):
    name = "jobFinder"
    start_urls = [
        'http://www.nelsonglobalgeek.com/ExampleScrapy.html',
    ]

    def parse(self, response):
        for row in response.css('div.row'):
            yield {
                'jobTitle': row.css('span.jobTitle a::text').extract(),
                'jobRate': row.css('span.jobRate::text').extract(),
                'jobDesc': row.css('span.jobDesc p::text').extract(),
                'jobURL': row.css('a::attr(href)').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
