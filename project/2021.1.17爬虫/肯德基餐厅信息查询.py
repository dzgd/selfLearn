'''
@Project ：project 
@File    ：肯德基餐厅信息查询.py
@IDE     ：PyCharm 
@Author  ：青崖@一白鹿
@Date    ：2021/1/17 11:39 
'''

import requests
import json
url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
address = input("enter a address : ")
data = {
    'cname': '',
    'pid': '',
    'keyword': address,
    'pageIndex': 1,
    'pageSize': 10
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

resp = requests.post(url = url , data =data , headers = headers)
dic_obj = resp.text
print(dic_obj)
fileName = address + '.json'
fp = open(fileName,'w',encoding='utf-8')
json.dump(dic_obj,fp=fp,ensure_ascii=False)
fp.close()
print("over!!!!")