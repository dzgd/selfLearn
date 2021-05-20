'''
@Project ：project 
@File    ：豆瓣电影.py
@IDE     ：PyCharm 
@Author  ：青崖@一白鹿
@Date    ：2021/1/16 23:54 
'''

import requests
import json
url = "https://movie.douban.com/j/chart/top_list"
param = {
    'type': 24,
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20,
}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}
resp = requests.get(url = url , params = param,headers=headers)
list_data = resp.json()
fp=open("./douban.json","w",encoding= "utf-8")
json.dump(list_data,fp = fp,ensure_ascii= False)
print("over!!!!")