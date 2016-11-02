__author__ = 'Ray'
from bs4 import BeautifulSoup
from mysql import insert_item
import requests
import  urllib2
import time
import pymongo



url = 'http://www.fsdpp.cn/sheji/'
urlbase = 'http://www.fsdpp.cn'

# client = pymongo.MongoClient('localhost',27017)
# chuangyi = client['chuangyi']
# keji = chuangyi['keji']
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
for one in range(4,10):
    url_req = url+ 'index_' + str(one) +'.html'
    print url_req
    htm_data = requests.get(url_req)
    htm_data.encoding='gbk'
    soup = BeautifulSoup(htm_data.text,'lxml')
    titles = soup.select('.entry-title > a')
    links = soup.select('div.entry-content > a')
    images = soup.select('div.entry-content > a > img')
    summarys = soup.select('div.entry-content > p')

    for title, link, image, summary in zip(titles,links,images,summarys):
        data = {
            'title':title.get_text(),
            'link':urlbase+link.get('href'),
            'image':urlbase + image.get('src'),
            'summary':summary.get_text(),
        }
        print data
        insert_item(data)
        #keji.insert_one(data)
    time.sleep(2)




# for item in keji.find():
#     print item['title']
