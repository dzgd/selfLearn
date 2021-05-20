# -*- coding: UTF-8 -*-
"""
@File    ：帮学姐.py
@Author  ：叶庭云
@CSDN    ：https://yetingyun.blog.csdn.net/
"""
import requests
import pandas as pd
from random import choice
from lxml import etree
import openpyxl
import logging
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import random

# print(random())
# 日志输出的基本配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['学校名称', '简称', '英文名称', '描述', '百度百科链接', '原始序号'])
df = pd.read_excel('学校名称.xlsx')['学校名称']
items = list(df.values)
# print(items)
# print(items.index('复旦大学'))

user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]


def get_data(item):
    try:
        # 记录一下它原本的序号
        sort_num = items.index(item)
        # 随机生成请求头
        headers = {
            'User-Agent':choice(user_agent)
        }
        # 构造的url
        url = f'https://baike.baidu.com/item/{item}'
        # 发送请求   获取响应
        rep = requests.get(url, headers=headers)
        sleep(random())
        # Xpath解析提取数据
        html = etree.HTML(rep.text)
        description = ''.join(html.xpath('/html/head/meta[4]/@content'))
        # 外文名
        en_name = '，'.join(html.xpath('//dl[@class="basicInfo-block basicInfo-left"]/dd[2]/text()')).strip()
        # 中文简称  有的话  是在dd[3]标签下
        simple_name = ''.join(html.xpath('//dl[@class="basicInfo-block basicInfo-left"]/dd[3]/text()')).strip()
        sheet.append([item, simple_name, en_name, description, url, sort_num])
        logging.info([item, simple_name, en_name, description, url, sort_num])

    except Exception as e:
        logging.info(e.args)
        pass


# 函数调用   开多线程
def run():
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_data, items)

    wb.save('成果.xlsx')
    print('===================== 数据成功下载完成 ======================')


run()