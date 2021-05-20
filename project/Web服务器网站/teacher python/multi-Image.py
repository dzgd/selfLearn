from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
import threading
def imageSpider(start_url):
    global threads
    global count
    try:
        urls=[]
        req=urllib.request.Request(start_url,headers=headers)
        data=urllib.request.urlopen(req)
        data=data.read()
        dammit=UnicodeDammit(data,["utf-8","gbk"])
        data=dammit.unicode_markup
        soup=BeautifulSoup(data,"lxml")
        images=soup.select("img")
        for image in images:
            try:
                src=image["src"]
                url=urllib.request.urljoin(start_url,src)
                if url not in urls:
                    print(url)
                    count=count+1
                    T=threading.Thread(target=download,args=(url,count))
                    T.setDaemon(False)
                    T.start()
                    threads.append(T)
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)
def download(url,count):
    try:
        if url[len(url)-4]==".":
            ext=url[len(url)-4:]
        else:
            ext=""
        req=urllib.request.Request(url,headers=headers)
        data=urllib.request.urlopen(req,timeout=100)
        data=data.read()
        fobj=open("images\\"+str(count)+ext,"wb")
        fobj.write(data)
        fobj.close()
        print("download"+str(count)+ext)
    except Exception as err:
        print(err)
start_url="http://www.weather.com.cn/weather/101270101.shtml"
headers={
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}
count=0
threads=[]
imageSpider(start_url)
for t in threads:
    t.join()
print("The End")

