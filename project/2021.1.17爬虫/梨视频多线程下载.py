'''
@Project ：project 
@File    ：梨视频多线程下载.py
@IDE     ：PyCharm 
@Author  ：青崖@一白鹿
@Date    ：2021/1/17 16:29 
'''

import requests
import json
from lxml import etree
from multiprocessing import Pool
import os
if not os.path.exists('./video.mp4'):
    os.mkdir('./video.mp4')
url = 'https://www.pearvideo.com/category_130'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
resp_text = requests.get(url = url,headers = headers).text
tree = etree.HTML(resp_text)
li_list = tree.xpath('//*[@id="listvideoListUl"]/li | //*[@id="categoryList"]/li')
base_url = 'https://www.pearvideo.com/videoStatus.jsp'
mp4_url = []
for li in li_list:
    detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
    Num = detail_url.split('_')[-1]
    #print(detail_url, name,Num)
    param = {
    'contId': Num
    }
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Referer': 'https://www.pearvideo.com/video_' + str(Num)
    }
    add_mp4 = requests.get(url=base_url,params=param,headers = header).json()['videoInfo']['videos']['srcUrl']
    print(add_mp4)
    add_list = add_mp4.split('-')
    new_add_list = add_list[0].split('/')
    new_add_list[-1] = 'cont-' + Num
    new_add_mp4 = '/'.join(new_add_list) + '-' + '-'.join(add_list[1:])
    print(new_add_mp4)
    dic = {
        'name':name,
        'url_mp4':new_add_mp4
    }
    mp4_url.append(dic)
print(mp4_url)
def get_video_data(dic):
    url = dic['url_map4']
    print(dic['name'],'正在下载........')
    video = requests.get(url = url ,headers = headers).content
    fileName = 'video.mp4' + '/' + dic["name"] +".mp4"
    count = 0
    with open(fileName,'wb') as fp:
        fp.write(video)
        count+=1
        print('下载完成第%d个'%(count))

print(len(mp4_url))
pool = Pool(12)
pool.map(get_video_data , mp4_url)
pool.close()
pool.join()


# https://www.pearvideo.com/video_1716101 尝尝国王之酒.mp4 1716101
# https://www.pearvideo.com/video_1714668 北京微旅行一：重新探索这座朝夕相伴的城市.mp4 1714668
# https://video.pearvideo.com/mp4/third/20210103/cont-1714668-15690592-155414-ld.mp4
#
# https://video.pearvideo.com/mp4/third/20210103/1610873862787-15690592-155414-ld.mp4
