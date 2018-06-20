# import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from dingdian.items import DingdianItem
class Myspider(scrapy.Spider):
    # http://www.23us.so/list/1_1.html
    name = "23us"
    allowed_domains = ['23us.so']
    base_url = 'http://www.23us.so/list/'
    baseurl = '.html'
    # 每个大类的链接
    def start_requests(self):
        for i in range(1,9):
            url = self.base_url + str(i) + '_1' +self.baseurl
            yield Request(url,self.parse)

    # 每一页
    def parse(self, response):
        max_page = BeautifulSoup(response.text,'lxml').find('div',class_='pagelink').find_all('a')[-1].get_text()
        bashurl = str(response.url)[:-7]
        for num in range(1,int(max_page)+1):
            url = bashurl + '_' +str(num) + self.baseurl
            yield Request(url,self.get_name)

    # 每本小说
    def get_name(self,response):
        tds = BeautifulSoup(response.text,'lxml').find_all('tr',bgcolor="#FFFFFF")
        for td in tds:
            # 小说名字
            novelname = td.find('a').get_text()
            # 小说链接
            novelurl = td.find('a')['href']
            yield Request(novelurl,callback=self.get_chapterurl,meta={'name':novelname,'url':novelurl})

    #进入某本小说的详情页
    def get_chapterurl(self,response):
        item = DingdianItem()
        # 小说名称
        item['name'] = response.meta['name']
        # 小说详情页
        item['novelurl'] = response.meta['url']
        # 分类
        item['category'] = BeautifulSoup(response.text,'lxml').find('table').find('a').get_text()
        # 作者
        item['author'] = BeautifulSoup(response.text,'lxml').find('table').find_all('td')[1].get_text().replace("\xa0",'')
        # 最新章节
        item['new'] = BeautifulSoup(response.text,'lxml').find('p',class_='btnlinks').find('a',class_='read')['href']
        return item
