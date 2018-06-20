# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .sql import Sql
from dingdian.items import DingdianItem
class DingdianPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,DingdianItem):
            name = item['name']
            ret = Sql.selecct(name)
            if ret[0] == 1:
                print(name+"已经保存了不需要再次保存")
                pass
            else:
                print(name + "正在保存")
                name = item['name']
                author = item['author']
                category = item['category']
                new = item['new']
                novelurl = item['novelurl']

                Sql.insert(name,author,category,novelurl,new)
                print("保存成功")

