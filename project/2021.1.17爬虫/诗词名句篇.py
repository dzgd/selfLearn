'''
@Project ：project 
@File    ：诗词名句篇.py
@IDE     ：PyCharm 
@Author  ：青崖@一白鹿
@Date    ：2021/1/17 12:36 
'''


import requests
from bs4 import BeautifulSoup
url = 'https://www.shicimingju.com/book/xiyouji.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
resp_text = requests.get(url = url,headers = headers).text
soup = BeautifulSoup(resp_text,'lxml')
li_list = soup.select('.book-mulu > ul > li')
fp = open('./xiyouji.txt','w',encoding= 'utf-8')
for li in li_list:
    title = li.a.string
    detail_url = 'https://www.shicimingju.com' +li.a['href']
    detail_page_text = requests.get(url = detail_url,headers = headers).text
    detail_soup = BeautifulSoup(detail_page_text,'lxml')
    content = detail_soup.find('div',class_='chapter_content').text
    fp.write(title+":"+content+"\n")
fp.close()
print("爬取成功!!!")