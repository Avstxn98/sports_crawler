import scrapy
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class SkySportsSpider(scrapy.Spider):
    name = "sky_sports"
    start_urls = ['https://www.skysports.com/']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.news_list = []

    def parse(self, response):
        for article in response.css('div.news-list__item.news-list__item--show-thumb-bp30'):
            self.news_list.append({
                'title': article.css('h4::text').get(),
                'link': article.css('a::attr(href)').get(),
            })

class BbcSportsSpider(scrapy.Spider):
    name = "bbc_sports"
    start_urls = ['https://www.bbc.com/sport']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.news_list = []

    def parse(self, response):
        for article in response.css('div.gs-c-promo'):
            title = article.css('h3::text').get()
            link = article.css('a::attr(href)').get()
            if link and link.startswith('/'):
                link = 'https://www.bbc.com' + link
            self.news_list.append({
                'title': title,
                'link': link,
            })

def fetch_news(spider_cls, result_list):
    process = CrawlerProcess()
    spider = spider_cls
    process.crawl(spider)
    process.start()
    result_list.extend(spider().news_list)

