'''
@Project ：project 
@File    ：spider_bilibili_danmu.py
@IDE     ：PyCharm 
@Author  ：青崖@一白鹿
@Date    ：2020/12/14 21:17 
'''
import requests #请求网页数据
from bs4 import BeautifulSoup #美味汤解析数据
import pandas as pd

def get_bilibili_url(start, end):
    url_list = []
    date_list = [i for i in pd.date_range(start, end).strftime('%Y-%m-%d')]
    for date in date_list:
        url = f"https://api.bilibili.com/x/v2/dm/history?type=1&oid=95640216&date={date}"
        url_list.append(url)
    return url_list

def get_bilibili_danmu(url_list):
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "cookie": "_uuid=572B80AB-F017-3D21-7168-1A9F3FE8633431141infoc; buvid3=D602B598-36FC-489A-AC7C-01438CE06C66138365infoc; sid=8plwub6l; DedeUserID=301363083; DedeUserID__ckMd5=aeb690ab4b8087bd; SESSDATA=581b1d26%2C1619073212%2C96bde*a1; bili_jct=a05f35ea70c738803960a5e41193500b; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(k|~k~ku~~Y0J'uY|Jlkuk~Y; PVID=3; bfe_id=1bad38f44e358ca77469025e0405c4a6" #Headers中copy即可
               }

    file = open("bilibili_danmu.txt", 'w', encoding = "utf-8")
    for i in range(len(url_list)):
        url = url_list[i]
        response = requests.get(url, headers=headers)
        response = response.content.decode("utf-8")  # 设置解码类型
        #print(response)
        soup = BeautifulSoup(response,"lxml")
        print(soup)
        data = soup.find_all("d")
        print(data)
        danmu = [data[i].text for i in range(len(data))]
        for items in danmu:
            file.write(items)
            file.write("\n")
    file.close()


if __name__ == "__main__":
    start = '12/10/2020' #设置爬取弹幕的起始日
    end = '12/14/2020' #设置爬取弹幕的终止日
    url_list = get_bilibili_url(start, end)
    get_bilibili_danmu(url_list)
    print("弹幕爬取完成")