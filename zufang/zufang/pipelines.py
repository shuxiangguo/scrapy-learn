# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class ZufangPipeline(object):

    def open_spider(self, spider):
        self.con = sqlite3.connect("zufang.sqlite")
        self.cur = self.con.cursor()

    def process_item(self, item, spider):

        # 获取当前将数据传入的爬虫名称
        print(spider.name)

        print('pipelines')

        insert_sql = "insert into zufang (title, money) VALUES ('{}', '{}')"\
            .format(item['title'], item['money'])
        print(insert_sql)
        self.cur.execute(insert_sql)
        self.con.commit()
        return item


    def spider_close(self, spider):
        self.con.close()
