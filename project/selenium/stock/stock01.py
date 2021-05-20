# import time
# from selenium import webdriver
# import pymysql
# source_url = 'http://quote.eastmoney.com/center/gridlist.html'
# class Spider:
#     def start(self,broad):
#         self.driver=webdriver.Chrome()
#         self.driver.get(source_url+broad)
#
#     def createtable(self,tablename):
#         try:
#             self.cursor.execute("drop table "+tablename[1:3])
#         except:
#             pass
#         self.cursor.execute("create table "+tablename[1:3]+"(count int,id varchar(16),name varchar(16),new_price varchar(16),up_rate varchar(16),down_rate varchar(16),pass_number varchar(16),pass_money varchar(16),rate varchar(16),highest varchar(16),lowest varchar(16),today varchar(16),yesterday varchar(16));")
#
#     def connect(self):
#         self.con = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="dujin",
#                               charset="utf8")
#         self.cursor = self.con.cursor(pymysql.cursors.DictCursor)
#         self.cursor.execute("delete from share")
#         opened = True
#         self.count = 0
#
#     def close(self):
#         self.con.close()
#
#     def share(self,broad,num):
#         lis = self.driver.find_elements_by_xpath("//*[@id='table_wrapper-table']/tbody/tr")
#         for li in lis:
#             self.count += 1
#             if self.count>num:
#                 break
#             print(li.text)
#             l=li.find_elements_by_xpath("./td")
#             self.cursor.execute(
#                 "insert into "+broad[1:3]+"(count,id,name,new_price,up_rate,down_rate,"
#                 "pass_number,pass_money,rate,highest,lowest,today,yesterday)"
#                 "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
#                 (self.count, l[1].text, l[2].text, l[6].text, l[7].text, l[8].text,
#                  l[9].text, l[10].text, l[11].text, l[12].text, l[13].text,
#                  l[14].text, l[15].text))
#         self.con.commit()
#         if self.count>num:
#             return
#         # try:
#         g = self.driver.find_element_by_xpath("//*[@id='main-table_paginate']/a[2]")
#         g.click()
#         time.sleep(3)
#         self.share(broad, num)
#         # except :
#         #     print("done")
#
#     def run(self,broad,num):
#         self.start(broad)
#         self.connect()
#         self.createtable(broad)
#         self.share(broad,num)
#         self.close()
# s= Spider()
# print("请选择爬取板块：\n"
#       "1.沪深A股\n"
#       "2.上证A股\n"
#       "3.深证A股\n")
# broad=input()
# n=eval(input("爬取的股票数量："))
# if broad=='1':
#     s.run("#hs_a_board",n)
# if broad=='2':
#     s.run("#sh_a_board",n)
# if broad=='3':
#     s.run("#sz_a_board",n)


import time
from selenium import webdriver
import pymysql
source_url = 'http://quote.eastmoney.com/center/gridlist.html'
class Spider:
    def start(self,broad):
        self.driver=webdriver.Chrome()
        self.driver.get(source_url+broad)

    def createtable(self,tablename):
        try:
            self.cursor.execute("drop table "+tablename[1:3])
        except:
            pass
        self.cursor.execute("create table "+tablename[1:3]+"(count int,id varchar(16),name varchar(16),new_price varchar(16),up_rate varchar(16),down_rate varchar(16),pass_number varchar(16),pass_money varchar(16),rate varchar(16),highest varchar(16),lowest varchar(16),today varchar(16),yesterday varchar(16));")

    def connect(self):
        self.con = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="dujin",
                              charset="utf8")
        self.cursor = self.con.cursor(pymysql.cursors.DictCursor)
        opened = True
        self.count = 0

    def close(self):
        self.con.close()

    def share(self,broad,num):
        lis = self.driver.find_elements_by_xpath("//*[@id='table_wrapper-table']/tbody/tr")
        for li in lis:
            self.count += 1
            if self.count>num:
                break
            print(li.text)
            l=li.find_elements_by_xpath("./td")
            self.cursor.execute(
                "insert into "+broad[1:3]+"(count,id,name,new_price,up_rate,down_rate,"
                "pass_number,pass_money,rate,highest,lowest,today,yesterday)"
                "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (self.count, l[1].text, l[2].text, l[6].text, l[7].text, l[8].text,
                 l[9].text, l[10].text, l[11].text, l[12].text, l[13].text,
                 l[14].text, l[15].text))
        self.con.commit()
        if self.count>num:
            return
        # try:
        g = self.driver.find_element_by_xpath("//*[@id='main-table_paginate']/a[2]")
        g.click()
        time.sleep(1)
        self.share(broad, num)
        # except :
        #     print("done")

    def run(self,broad,num):
        self.start(broad)
        self.connect()
        self.createtable(broad)
        self.share(broad,num)
        self.close()
s= Spider()
print("请选择爬取板块：\n"
      "1.沪深A股\n"
      "2.上证A股\n"
      "3.深证A股\n")
broad=input()
n=eval(input("爬取的股票数量："))
if broad=='1':
    s.run("#hs_a_board",n)
if broad=='2':
    s.run("#sh_a_board",n)
if broad=='3':
    s.run("#sz_a_board",n)
