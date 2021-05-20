
###使用递归程序实现深度优先遍历
'''from bs4 import BeautifulSoup
import urllib.request
def spider(url):
    try:
        data=urllib.request.urlopen(url)
        data=data.read()
        data=data.decode()
        soup=BeautifulSoup(data,"lxml")
        print(soup.find("h3").text)
        links=soup.select("a")
        for link in links:
            href=link["href"]
            url=start_url+"/"+href
            spider(url)
    except Exception as err:
        print(err)
start_url="http://127.0.0.1:5000"
spider(start_url)
print("The End")'''




######使用栈来深度优先爬取数据
from bs4 import BeautifulSoup
import urllib.request
class Stack:
    def __init__(self):
        self.st=[]
    def push(self,obj):              #进栈函数
        self.st.append(obj)
    def pop(self):                   #出栈函数（栈顶先出，即后进先出）
        return self.st.pop()
    def empty(self):
        return len(self.st)==0
def spider(url):
    stack=Stack()
    stack.push(url)
    while not stack.empty():
        url=stack.pop()
        try:
            data=urllib.request.urlopen(url)
            data=data.read()
            data=data.decode()
            soup=BeautifulSoup(data,"lxml")
            print(soup.find("h3").text)
            links=soup.select("a")
            for i in range(len(links)-1,-1,-1):         #倒序排列
                href=links[i]["href"]
                url=start_url+"/"+href
                stack.push(url)
        except Exception as err:
            print(err)
start_url="http://127.0.0.1:5000"
spider(start_url)
print("The End")


######使用队列进行广度优先爬取数据
from bs4 import BeautifulSoup
import urllib.request
class Queue:
    def __init__(self):
        self.st=[]
    def enter(self,obj):         #入列函数
        self.st.append(obj)
    def fetch(self):             #出列函数
        return self.st.pop()
    def empty(self):
        return len(self.st)==0
def spider(url):
    queue=Queue()
    queue.enter(url)
    while not queue.empty():
        url=queue.fetch()
        try:
            data=urllib.request.urlopen(url)
            data=data.read()
            data=data.decode()
            soup=BeautifulSoup(data,"lxml")
            print(soup.find("h3").text)
            links=soup.select("a")
            for link in links:
                href=link["href"]
                url=start_url+"/"+href
                queue.enter(url)
        except Exception as err:
            print(err)
start_url="http://127.0.0.1:5000"
spider(start_url)
print("The End")
