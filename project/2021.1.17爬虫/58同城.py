'''
@Project ：project 
@File    ：58同城.py
@IDE     ：PyCharm 
@Author  ：青崖@一白鹿
@Date    ：2021/1/17 13:20 
'''

import requests
from lxml import etree
url = 'https://cs.58.com/ershoufang/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
resp_text = requests.get(url = url,headers = headers).text
tree = etree.HTML(resp_text)
li_list = tree.xpath('/html/body/div[5]/div[5]/div[1]/ul/li')
fp = open('./58.txt','w',encoding='utf-8')
for li in li_list:
    title = li.xpath('./div[2]/h2/a/text()')[0]
    big1 =li.xpath('./div[2]/p[1]/span/text()')
    big2 =li.xpath('./div[2]/p[2]/span/a/text()')
    big3 =[i for i in li.xpath('./div[2]/div/span/text()') if i!="="]
    str1 = ' '.join(big1)
    str2 = ' '.join(big2)
    str3 = ' '.join(big3)
    fp.write(title+"\n"+str1+"\n"+str2+"\n"+str3+"\n\n")

fp.close()
print("over!!!")