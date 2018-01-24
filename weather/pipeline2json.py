import time
import json
import codecs
import csv

class WeatherPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        fileName = today+'.json'
        with codecs.open(fileName,'a',encoding='utf8') as fp:
            line = json.dumps(dict(item),ensure_ascii=False)+'\n'
            fp.write(line)
        fileName1 = today+'.csv'
        fieldnames=['city','cityDate','temp','weather','wind']
        with codecs.open(fileName1,'a') as fp:
            writer = csv.DictWriter(fp,fieldnames=fieldnames)
           # writer.writeheader()
            writer.writerow({'city':item['city'],
                             'cityDate':item['cityDate'][0],
                             'temp':item['temp'],
                             'weather':item['weather'],
                             'wind':item['wind']})
        return item
