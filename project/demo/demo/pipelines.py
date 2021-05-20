# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

#
# class DemoPipeline:
#     def process_item(self, item, spider):
#         return item

import pymysql

class BookPipeline(object):
    def open_spider(self, spider):
        print("opened")
        self.count = 0
        try:
            self.con = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", charset="utf8",db = "dujin")
            self.cursor = self.con.cursor(pymysql.cursors.DictCursor)
            try:
                self.cursor.execute("drop table books")
            except:
                pass
            try:
                sql = "create table books(bTitle varchar(512) primary key,bAuthor varchar(256),bPublisher varchar(256),bDate varchar(32),bPrice varchar(16),bDetail text)"
                self.cursor.execute(sql)
            except:
                self.cursor.execute("delete from books")
            self.opened = True
        except Exception as err:
            print(err)
            self.opened = False

    def close_spider(self, spider):
        if self.opened: self.con.commit()

        self.con.close()
        self.opened = False
        print("closed")
        print("总共爬取", self.count, "本书籍")

    def process_item(self, item, spider):
        try:
            print(item["title"])
            print(item["author"])
            print(item["publisher"])
            print(item["date"])
            print(item["price"])
            print(item["detail"])
            print()
            if self.opened:
                self.cursor.execute(
                    "insert into books (bTitle,bAuthor,bPublisher,bDate,bPrice,bDetail) values(%s,%s,%s,%s,%s,%s)",
                    (item["title"], item["author"], item["publisher"], item["date"], item["price"], item["detail"]))
                self.count += 1
        except Exception as err:
            print(err)
        return item