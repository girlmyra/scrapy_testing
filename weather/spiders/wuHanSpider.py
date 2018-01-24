# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class WuhanspiderSpider(scrapy.Spider):
    name = 'wuHanSpider'
    allowed_domains = ['weather.com.cn']
    def start_requests(self):
        city_numbers={'beijing':'101010100.shtml',
                  'shenzhen':'101280601.shtml'}
        urls=[]
        for k,v in city_numbers.items():
            urls.append('http://www.weather.com.cn/weather/'+v)
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        city_numbers={'beijing':'101010100.shtml',
                     'shenzhen':'101280601.shtml'}
        subSelector=response.xpath('//div[@id="7d"]/ul/li')
        items=[]
        page=response.url.split("/")[-1]
        for k,v in city_numbers.items():
            if page == v:
                city = k
        for sub in subSelector:
            item=WeatherItem()
            temp=[]
            item['city'] = city
            item['cityDate']=sub.xpath('./h1/text()').extract()
            temp1 = sub.css('p.tem span::text').extract()
            temp2 = sub.css('p.tem i::text').extract()
            temp = temp1 + temp2
            item['temp'] = '/'.join(temp)
            item['weather'] = sub.css('p.wea::text').extract()
            item['wind'] = sub.css('p.win i::text').extract()
            items.append(item)
        return items


            
