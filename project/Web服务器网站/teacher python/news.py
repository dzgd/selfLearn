'''
#####爬取中国旅游网要闻
from bs4 import BeautifulSoup
import requests
import re
import time
for i in range(58):
    i=i+1
    url="http://www.cntour.cn/news/list.aspx?tid=50&page="+str(i)
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
    data=requests.get(url,headers=headers)
    soup=BeautifulSoup(data.text,"lxml")
    data=soup.select("#main > div > div.newListBox.clearfix > div.leftBox > div.newsList > ul > li > a")
    for item in data:
        result={
                "title":item.get_text(),
                "link":item.get("href"),
                "ID":re.findall("\d+",item.get("href"))
             }
        print(result)
'''

