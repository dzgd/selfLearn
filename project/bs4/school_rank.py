# coding=UTF-8
import urllib.request
import pymysql
from scrapy.selector import Selector
url = "https://www.shanghairanking.cn/rankings/bcur/2020"
resp = urllib.request.urlopen(url)
data = resp.read()
html = data.decode()
try:
    con = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="dujin",
                          charset="utf8")
    cursor = con.cursor()
    try:
        cursor.execute("drop table school")
    except:
        pass
    try:
        sql = "create table school(id int(16) ,sch varchar(256),province varchar(256),kind varchar(256),score varchar(256),layer varchar(256))"
        cursor.execute(sql)
    except:
        cursor.execute("delete from school")
except Exception as err:
    print(err)

#print(html)
selector = Selector(text = html)
lst = selector.xpath("//table[@class='rk-table']/tbody//tr")
print(len(lst))
for l in lst:
    ts = l.xpath("./td/text()")
    school = l.xpath("./td[@class='align-left']/a/text()").extract_first().strip()
    b = ts.extract()
    a = []
    for i in b:
        j = i.strip()
        if j:
            a.append(j)
    #print(a)
    if len(a) ==5:
        cursor.execute(
            "insert into school(id,sch,province,kind,score,layer) values (%s,%s,%s,%s,%s,%s)",(a[0],school,a[1],a[2],a[3],a[4]))
    else:
        cursor.execute(
        "insert into school(id,sch,province,kind,score,layer) values (%s,%s,%s,%s,%s,%s)",(a[0], school, a[1], a[2], a[3], "-"))
    con.commit()
print("successfully")
