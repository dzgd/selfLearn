import requests    # 导入爬虫专有的request包来请求url
from bs4 import BeautifulSoup    # 导入bs4包把请求下来的源代码封装成对象

import time    # 导入时间模块
import csv    # 导入csv模块进行数据读取

# 定义爬取网页函数
def readpages(url,writer,sum):      # 设置三个参数，第一个是网址，第二个是封装的csv格式文件，第三个是设置翻页
    re = requests.get(url)    # 利用get请求url数据，得到响应
    soup = BeautifulSoup(re.text,'html.parser')    #  拿到响应回来的文本，封装成对象，利用html解析器
    viewlist = soup.find(class_='viewlist_ul').find_all('li')  # 利用soup的find函数定位element元素，找到属性为"viewlist_ul"下的所有li标签
    for i in viewlist:     # 利用for循环遍历li标签
        # print(i['carname'])   #  打印li标签下的汽车名字
        # print(i['regdate'])    #  打印li标签下的日期
        # print('公里数',i['milage'])    #打印li标签下的公里数
        # print('价格', i['price'])    #打印li标签下的价格
        # print(i['dealerid'])     #打印li标签下的汽车id
        # print(i['infoid'])     # 打印li标签下的汽车其他信息
        subPage = 'https://www.che168.com/dealer/'+i['dealerid']+'/'+i['infoid']+'.html'  #点击一辆汽车，出现的url为这种格式
        dangan = readSubPage(subPage)    # 利用定义的爬出子网页的函数深度爬取汽车的详细信息
        writer.writerow({'id': sum, '车型': i['carname'], '公里数': i['milage'], '价格': i['price'], '其他': str(dangan)})  #利用csv对象保存爬取的数据，格式为字段和对应的数据
        sum = sum+1   # 爬取一辆汽车就自加1，利用sum可以知道总共爬出多少辆汽车
        print('子网页抓取')   # 打印
        time.sleep(1)    #为防止封IP，爬取一辆车后暂停1毫秒
    nextpage = soup.find(class_='page-item-next')    # 利用soup的find方法找到下一页的标签，发现在属性为page-item-next里
    nexturl = 'https://www.che168.com/'+nextpage["href"]     # 拿到下一页的url连接
    print(nexturl)     # 打印
    print('下一页')   # 打印
    return nexturl    # 函数返回下一页的url


# 定义爬取子网页的函数
def readSubPage(subPage):     # 参数为子网页的url
    re = requests.get(subPage)   # 通过get请求响应url请求
    soup = BeautifulSoup(re.text, 'html.parser')   # 同理，实例化一个封装好的对象
    list = soup.find_all(class_='basic-item-ul')    #定位找到属性为basic-item-ul的element元素列表，为后面爬取定位
    if list is not None:      # 如果有属性为basic-item-ul的element元素列表，就遍历列表，爬取每个列表下的文本信息
        s = ''
        for i in list:
            print(i)
            s = s+str(i.text)
        return s
    else:
        return ''
if __name__ == '__main__':    # 运行主程序
    #第一页网址：
    file = open('data//cars.csv', 'a',encoding='utf-8')    # 打开此目录下的cSV文件，以追加的方式把爬取的数据保存进此csv文件中
    writer = csv.DictWriter(file,fieldnames = ['id','车型','公里数','价格','其他'])   # 初始化csv文件和相应的字段
    writer.writeheader()     #   把初始化的参数写入文件的开头好识别
    url = "https://www.che168.com/chongqing/baoma/#pvareaid=108402#listfilterstart"    # 最开始的url网址，为二手车之家
    sum = 0   # 从第一页开始爬取
    while url is not None:    # 利用while循环知道爬取到最后一页
        url = readpages(url,writer,sum)    # 利用封装的函数进行爬取，返回下一页的url网址

