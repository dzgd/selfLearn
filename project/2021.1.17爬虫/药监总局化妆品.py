'''
@Project ：project 
@File    ：药监总局化妆品.py
@IDE     ：PyCharm 
@Author  ：青崖@一白鹿
@Date    ：2021/1/17 11:52 
'''

'''
<div class="thumb">

<a href="/article/123972809" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12397/123972809/medium/F7IPN6AAXLJ8HFDB.jpg" alt="糗事#123972809" class="illustration" width="100%" height="auto">
</a>
</div>
'''

# 解析正则表达式
# ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'

import requests
import re
import os
if not os.path.exists('./qiutuLibs'):
    os.mkdir('./qiutuLibs')

    url = 'https://www.qiushibaike.com/imgrank/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    page_text = requests.get(url = url,headers = headers).text
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex,page_text,re.S)
    # src = https://pic.qiushibaike.com/system/pictures/12398/123987146/medium/GIQW2W7F0X8B6V3S.jpg
    for src in img_src_list:
        src = 'https:' + src
        img_data = requests.get(url = src,headers = headers).content
        fileName = src.split('/')[-1]
        imgPath = './qiutuLibs/'+fileName
        with open(imgPath,'wb') as fp:
            fp.write(img_data)
            print(fileName,"下载成功!!!")

