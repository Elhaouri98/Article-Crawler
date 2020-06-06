# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import dns
class ArticleCrawlerPipeline:
    def __init__(self):
        #setting up the connection with the atlas cluster
        self.conn = pymongo.MongoClient('mongodb+srv://user:user@cluster0-kiqxz.gcp.mongodb.net/test', 27017)
        db = self.conn['theguardian']
        self.collection = db['articles']
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
