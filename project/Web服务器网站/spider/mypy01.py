# from bs4 import BeautifulSoup
# doc='''
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">
# Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.
# </p>
# <p class="story">...</p>
# </body>
# </html>
# '''
# soup=BeautifulSoup(doc,"lxml")
# s=soup.prettify()
#print(s)


##################爬天气预报########2020/3/24##########
'''<ul class="t clearfix">
<li class="sky skyid lv2 on">
<h1>24日（今天）</h1>
<big class="png40"></big>
<big class="png40 n01"></big>
<p title="多云" class="wea">多云</p>
<p class="tem">
<i>16℃</i>
</p>
<p class="win">
<em>
<span title="无持续风向" class="NNW"></span>
</em>
<i>&lt;3级</i>
</p>
<div class="slid"></div>
</li>
<li class="sky skyid lv3">
<h1>25日（明天）</h1>
<big class="png40 d02"></big>
<big class="png40 n01"></big>
<p title="阴转多云" class="wea">阴转多云</p>
<p class="tem">
<span>23℃</span>/<i>16℃</i>
</p>
<p class="win">
<em>
<span title="无持续风向" class="NNW"></span>
<span title="无持续风向" class="NNW"></span>
</em>
<i>&lt;3级</i>
</p>
<div class="slid"></div>
</li>
<li class="sky skyid lv3">
<h1>26日（后天）</h1>
<big class="png40 d02"></big>
<big class="png40 n07"></big>
<p title="阴转小雨" class="wea">阴转小雨</p>
<p class="tem">
<span>21℃</span>/<i>12℃</i>
</p>
<p class="win">
<em>
<span title="无持续风向" class="NNW"></span>
<span title="无持续风向" class="NNW"></span>
</em>
<i>&lt;3级</i>
</p>
<div class="slid"></div>
</li>
<li class="sky skyid lv1">
<h1>27日（周五）</h1>
<big class="png40 d00"></big>
<big class="png40 n02"></big>
<p title="晴转阴" class="wea">晴转阴</p>
<p class="tem">
<span>19℃</span>/<i>11℃</i>
</p>
<p class="win">
<em>
<span title="无持续风向" class="NNW"></span>
<span title="无持续风向" class="NNW"></span>
</em>
<i>&lt;3级</i>
</p>
<div class="slid"></div>
</li>
<li class="sky skyid lv3">
<h1>28日（周六）</h1>
<big class="png40 d07"></big>
<big class="png40 n07"></big>
<p title="小雨" class="wea">小雨</p>
<p class="tem">
<span>16℃</span>/<i>9℃</i>
</p>
<p class="win">
<em>
<span title="无持续风向" class="NNW"></span>
<span title="无持续风向" class="NNW"></span>
</em>
<i>&lt;3级</i>
</p>
<div class="slid"></div>
</li>
<li class="sky skyid lv3">
<h1>29日（周日）</h1>
<big class="png40 d02"></big>
<big class="png40 n07"></big>
<p title="阴转小雨" class="wea">阴转小雨</p>
<p class="tem">
<span>13℃</span>/<i>9℃</i>
</p>
<p class="win">
<em>
<span title="无持续风向" class="NNW"></span>
<span title="无持续风向" class="NNW"></span>
</em>
<i>&lt;3级</i>
</p>
<div class="slid"></div>
</li>
<li class="sky skyid lv3">
<h1>30日（周一）</h1>
<big class="png40 d02"></big>
<big class="png40 n07"></big>
<p title="阴转小雨" class="wea">阴转小雨</p>
<p class="tem">
<span>16℃</span>/<i>11℃</i>
</p>
<p class="win">
<em>
<span title="无持续风向" class="NNW"></span>
<span title="无持续风向" class="NNW"></span>
</em>
<i>&lt;3级</i>
</p>
<div class="slid"></div>
</li>
</ul>'''
# from bs4 import BeautifulSoup
# from bs4 import UnicodeDammit
# import urllib.request
# list=[101270101,101010100,101040100,101110101,101250101,101110405] #成都，北京,重庆，西安,长沙,定边的编号
# list1=["成都","北京","重庆","西安","长沙","定边"]
# i=0
# for num in list:
#     i+=1
#     print("{}的7天天气预报".format(list1[i-1]))
#     url="http://www.weather.com.cn/weather/"+str(num)+".shtml"
#     try:
#         headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
#         req=urllib.request.Request(url,headers=headers)
#         data=urllib.request.urlopen(req)
#         data=data.read()
#         dammit=UnicodeDammit(data,["utf-8","gbk"])
#         data=dammit.unicode_markup
#         soup=BeautifulSoup(data,"lxml")
#         lis=soup.select('ul[class="t clearfix"] li')
#         n=0
#         for li in lis:
#             try:
#                 date=li.select("h1")[0].text
#                 weather=li.select('p[class="wea"]')[0].text
#                 if n>0:
#                     temp=li.select('p[class="tem"] span')[0].text+"/"+li.select('p[class="tem"] i')[0].text
#                 else:
#                     temp=li.select('p[class="tem"] i')[0].text
#                 print(date,weather,temp)
#                 n=n+1
#             except Exception as err:
#                 print(err)
#
#     except Exception as err:
#         print(err)

######后台线程

'''import threading
import time
import random
def reading():
    for i in range(10):
        print("reading",i)
        time.sleep(random.randint(1,2))
r=threading.Thread(target=reading)
r.setDaemon(False)     #后台线程
r.start()
print("The End")'''


#######混合线程
import threading
import time
import random
def reading():
    for i in range(5):
        print("reading",i)
        time.sleep(random.randint(1,2))
def test():
    r=threading.Thread(target=reading)
    r.setDaemon(True)
    r.start()
    print("test end")
t=threading.Thread(target=test)
t.setDaemon(False)
t.start()
print("The End")