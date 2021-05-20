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

class SharePipeline:
    def open_spider(self, spider):
        print("opened")
        self.count = 0
        try:
            self.con = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="dujin",
                                       charset="utf8")
            self.cursor = self.con.cursor(pymysql.cursors.DictCursor)
            try:
                self.cursor.execute("drop table share01")
            except:
                pass
            try:
                sql = "create table share01(count int(16) primary key,id varchar(256),name varchar(256),new_price varchar(256),up_rate varchar(256),down_rate varchar(256),\
                    pass_number varchar(256),pass_money varchar(256),rate varchar(256),highest varchar(256),lowest varchar(256),today varchar(256),yesterday varchar(256))"
                self.cursor.execute(sql)
            except:
                self.cursor.execute("delete from share01")
            self.opened = True
        except Exception as err:
            print(err)
            self.opened = False
    def close_spider(self, spider):
        if self.opened: self.con.commit()

        self.con.close()
        self.opened = False
        print("closed")
        print("总共爬取", self.count, "个股市")

    def process_item(self, item, spider):
        try:
            if self.opened:
                self.count += 1
                self.cursor.execute(
                    "insert into share01(count,id,name,new_price,up_rate,down_rate,\
                    pass_number,pass_money,rate,highest,lowest,today,yesterday)\
                    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (self.count, item["id"], item["name"], item["new_price"], item["up_rate"], item["down_rate"],
                     item["pass_number"], item["pass_money"], item["rate"], item["highest"], item["lowest"],
                     item["today"], item["yesterday"]))
        except Exception as err:
            print(err)
        return item
