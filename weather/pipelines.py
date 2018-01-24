# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time 
import os.path
import urllib

class WeatherPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        fileName = today+'.txt'
        with open(fileName,'a') as fp:
            fp.write('City is: ' +item['city']+'\t\n')
            fp.write('Date is:' +item['cityDate'][0]+'\t\n')
            fp.write('temperature:' + item['temp']+'\t')
            fp.write('weather:' + item['weather'][0]+'\t')
            fp.write('wind:' + item['wind'][0]+'\t\n')   
        return item
