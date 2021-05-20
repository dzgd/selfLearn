from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
list=[101270101,101010100,101040100,101110101] #成都，北京,重庆，西安的编号
list1=["成都","北京","重庆","西安"]
i=0
for num in list:
    i+=1
    print("{}的7天天气预报".format(list1[i-1]))
    url="http://www.weather.com.cn/weather/"+str(num)+".shtml"
    try:
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
        req=urllib.request.Request(url,headers=headers)
        data=urllib.request.urlopen(req)
        data=data.read()
        dammit=UnicodeDammit(data,["utf-8","gbk"])
        data=dammit.unicode_markup
        soup=BeautifulSoup(data,"lxml")
        lis=soup.select('ul[class="t clearfix"] li')
        n=0
        for li in lis:
            try:
                date=li.select("h1")[0].text
                weather=li.select('p[class="wea"]')[0].text
                if n>0:
                    temp=li.select('p[class="tem"] span')[0].text+"/"+li.select('p[class="tem"] i')[0].text
                else:
                    temp=li.select('p[class="tem"] i')[0].text
                print(date,weather,temp)
                n=n+1
            except Exception as err:
                print(err)

    except Exception as err:
        print(err)
###############2020.3.11(晚)



