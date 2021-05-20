'''
@Project ：project 
@File    ：百度翻译.py
@IDE     ：PyCharm 
@Author  ：青崖@一白鹿
@Date    ：2021/1/16 23:37 
'''


import requests
import json
post_url = "https://fanyi.baidu.com/sug"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}
word = input("enter a word : ")
data = {
    "kw": word
}

resp = requests.post(url = post_url,data = data,headers = headers)
dic_obj = resp.json()
print(dic_obj)
fileName = word +".json"
fp =open(fileName,"w",encoding = "utf-8")
json.dump(dic_obj,fp = fp,ensure_ascii=False)
print("over!!!!!!")
