# coding=UTF-8
import urllib.request
import pymysql
from scrapy.selector import Selector
url = "http://fx.cmbchina.com/hq/"
resp = urllib.request.urlopen(url)
data = resp.read()
html = data.decode()
try:
    con = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="dujin",
                          charset="utf8")
    cursor = con.cursor()
    try:
        cursor.execute("drop table rate")
    except:
        pass
    try:
        sql = "create table rate(id varchar(256) primary key,code varchar(256),name varchar(256),relation varchar(256),shen varchar(256),fen varchar(256))"
        cursor.execute(sql)
    except:
        cursor.execute("delete from rate")
except Exception as err:
    print(err)

#print(html)
selector = Selector(text = html)
lst = selector.xpath("//div[@id='realRateInfo']//tr")
for l in lst:
    ts = l.xpath("./td/text()")
    b = ts.extract()
    a = []
    for i in b:
        if i:
            a.append(i.strip())
    cursor.execute(
        "insert into rate(id,code,name,relation,shen,fen)values (%s,%s,%s,%s,%s,%s)",(a[0],a[1],a[2],a[3],a[4],a[5]))
    con.commit()
print("sucessefully")
