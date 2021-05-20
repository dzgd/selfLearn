# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class PopulationInfoPipeline:
#     def process_item(self, item, spider):
#         return item

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

#
# class Share01Pipeline:
#     def process_item(self, item, spider):
#         return item

import pymysql

class PopulationInfoPipeline:
    def open_spider(self, spider):
        print("opened")
        self.count = 0
        try:
            self.con = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="dujin",
                                       charset="utf8")
            self.cursor = self.con.cursor(pymysql.cursors.DictCursor)
            try:
                self.cursor.execute("drop table population")
            except:
                pass
            try:
                sql = "create table population(id int(16) primary key,code varchar(256),name varchar(256),relation varchar(256),shenfenzhenghaoma varchar(256))"
                self.cursor.execute(sql)
            except:
                self.cursor.execute("delete from population")
            self.opened = True
        except Exception as err:
            print(err)
            self.opened = False
    def close_spider(self, spider):
        if self.opened: self.con.commit()

        self.con.close()
        self.opened = False
        print("closed")
        print("总共爬取", self.count, "条数据")

    def process_item(self, item, spider):
        try:
            if self.opened:
                self.count += 1
                self.cursor.execute(
                    "insert into population(id,code,name,relation,shenfenzhenghaoma)\
                    values (%d,%s,%s,%s,%s)",
                    ( item["id"], item["code"], item["name"], item["relation"], item["shenfenzhenghaoma"]))
        except Exception as err:
            print(err)
        return item

