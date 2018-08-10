import scrapy
import time

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.conf import settings 
from selenium import webdriver
from keyhole.items import *
from selenium.webdriver.chrome.options import Options
import datetime
from scrapy.selector import Selector


class KeyholeSpiderFacebook(CrawlSpider):
    
    name = 'keyhole_facebook'

    def start_requests(self):
        url = 'http://keyhole.co/'

        yield scrapy.Request(url=url, callback=self.parseFacebook)
    
    
    def parseFacebook(self, response):
        
        keyhole = KeyholeFacebookItem()
        
        keyhole['source'] = self.name
        keyhole['platform'] = "Facebook"
        keyhole['name'] = response.xpath('//*[@id="account"]/div/div[1]/div[1]/div[2]/div/a/p/text()').extract_first()

        creationdate = getattr(self, 'time', None)
        if creationdate is not None:
            keyhole['date'] = datetime.datetime.strptime(creationdate,settings['DATE_FORMAT'])
        else:
            keyhole['date'] = datetime.datetime.strptime(str(datetime.datetime.now().isoformat()), settings['DATE_FORMAT'])
            

        keyhole['pageLikes'] = response.xpath('//div[@class="page-likes"]/p/text()').extract_first()
        keyhole['avgLikes'] = int(response.xpath('//div[@class="avg-likes"]/p/text()').extract_first().replace(',',''))
        keyhole['avgComments'] = int(response.xpath('//div[@class="avg-comments"]/p/text()').extract_first().replace(',',''))
        keyhole['avgShares'] = int(response.xpath('//div[@class="avg-shares"]/p/text()').extract_first().replace(',',''))
        keyhole['avgEngRate'] = float(response.xpath('//div[@class="avg-engRate"]/p/text()').extract_first()[:-1])

        yield keyhole