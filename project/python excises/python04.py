'''首先分析定向爬虫的可行性
进入网址：http://s.taobao.com/robots.txt  查看
发现禁止爬取，但是可以以类人类行为进行爬取。作为教学实例。'''
'''import requests
import re
import pandas as pd
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)  #时间限制为30秒
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "失败"
def parserPage(ilt,html):
    try:          #返回商品名称的列表，？是最小匹配。加\是为了转义。
        ns=re.findall(r'\"raw_title\"\:\".*?\"',html)        #返回价格的列表，[\d\.]*这个好好消化
        jiage=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)        #返回已购人数列表
        renshu=re.findall(r'\"view_sales\"\:\".*?\"',html)
        for i in range(len(ns)):            #将raw_title去掉，eval函数的意思是吧返回的字符串中的最外层单引号或双引号去掉。
            name=eval(ns[i].split(':')[1])
            price=eval(jiage[i].split(':')[1])
            people=eval(renshu[i].split(':')[1])
            ilt.append([price,people,name])
    except:
        print("")
def saveGoodsList(ilt):
    ilts=[]
    for j in ilt:
        ilts.append([j[0],j[1].split('人')[0],j[2]])
    fpath=r'D:\wangluopachongfile\chenshan.xlsx'
    a=pd.DataFrame(ilts,columns=['价格','已购人数','商品名称'])
    a.to_excel(fpath)
def main():
    goods="衬衫"   #指定商品名称
    depth=2      #指定爬取的页面个数
    start_url='https://s.taobao.com/search?q='+goods
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+"&s="+str(44*i)
            html=getHTMLText(url)
            parserPage(infoList,html)
        except:
            continue
    saveGoodsList(infoList)
main()'''


#############          Flask网页简单编写     ##################    结果:http://127.0.0.1:5000/
'''import flask
app=flask.Flask(__name__)
@app.route("/")
def index():
    f=open("index.html","rb")
    data=f.read()
    f.close()
    return data
app.run()'''


import requests
from bs4 import BeautifulSoup
url="http://www.baidu.com"
r=requests.get(url)
r.encoding=r.apparent_encoding
demo=r.text
soup=BeautifulSoup(demo,"lxml")
#tags=soup.find_all("a")
#for tag in tags:
#    print(tag["href"])
tags=soup.find_all("p")
for tag in tags:
    print(tag.text)
