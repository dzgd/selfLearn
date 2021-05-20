'''import requests
from bs4 import BeautifulSoup
import bs4
def getHTWLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "爬取失败"
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tag in soup.find("tbody").children:
        if isinstance(tag,bs4.element.Tag):
            tds=tag("td")
            ulist.append([tds[0].string,tds[1].string,tds[3].string])
def printUnivList(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u =ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
def main():
    uinfo=[]
    url="http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html"
    html=getHTWLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,100)
main()'''

################################################################################################
'''from bs4 import BeautifulSoup
import requests
r=requests.get("http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html")
r.encoding=r.apparent_encoding
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
print(soup.find_all("tbody"))
for tag in soup.find_all(True):
    print(tag.name)  '''             # 访问网页的所有标签名字



'''for tag in soup.find_all(re.compile("t")):
    print(tag.name)'''            # 访问以“t”开头的标签名字，使用正则表达式

################网络淘宝爬虫#########################################################################

'''import requests
import re
def getHTMLText(url,kv,cookies):
    try:
        r = requests.get(url, headers=kv,cookies=cookies,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            #eval函数执行一个字符串表达式
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")
#输入到屏幕
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:25}"
    #打印表头
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
#主函数
def main():
    goods = '联想笔记本'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    coo='t=41653b20706345d12631aafb017b970f; cna=wKFrFnvBNRsCAXyATYJvStxu; thw=cn; v=0; cookie2=161c76018f25b9311c464719c2aa38ba; _tb_token_=e683b3559e733; unb=2212782603; uc3=lg2=UIHiLt3xD8xYTw%3D%3D&vt3=F8dByuqh437%2Fb%2FHhiE4%3D&id2=UUpgRKr%2BqoQHqA%3D%3D&nk2=pbJvuSGAeVW8Zg%3D%3D; csg=fa67ab25; lgc=%5Cu8D77%5Cu98CE%5Cu4E86%5Cu7A57%5Cu5B50; cookie17=UUpgRKr%2BqoQHqA%3D%3D; dnk=%5Cu8D77%5Cu98CE%5Cu4E86%5Cu7A57%5Cu5B50; skt=95221cd1c2aa6cc0; existShop=MTU3NzE2OTIzNA%3D%3D; uc4=nk4=0%40pwW3VMB6m4v7c%2B1Av8qXNXHpKjuL&id4=0%40U2gqy1t91FKKDK9ChmZT%2BdsbZc8w; tracknick=%5Cu8D77%5Cu98CE%5Cu4E86%5Cu7A57%5Cu5B50; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=%E5%AD%9032; _nk_=%5Cu8D77%5Cu98CE%5Cu4E86%5Cu7A57%5Cu5B50; cookie1=WvcYr4FuAHzJNq3CI7IDe0Vs2KH66XulIazTWuEHUKc%3D; enc=ZD%2B5tM4n0urXXyxYIdz7Z4LiPZNpca1RbpyqDcJbXdWrbo8pPCGUegPxhgUbAxO8z9dvygzlF3kQtcGOKB%2B%2FiA%3D%3D; mt=ci=91_1; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTbmhFo9Fy9aA%3D%3D&cookie15=W5iHLLyFOGW7aA%3D%3D; JSESSIONID=9AF926C20DC6A16E96A28DA11B9E3E84; l=cBP5-TLVq8T4HoOsBOCwourza77OSIRAguPzaNbMi_5CL6L66QbOoj_xYFp6VjWdTp8B4Ydbw2w9-etui-y06Pt-g3fP.; isg=BBYWvAMGVOBtyGOtf5Y7ZEB6Z8wYt1rxxS69T4B_AvmUQ7bd6EeqAXyx258Ka1IJreferer: https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
    cookies={}
    for line in coo.split(';'):
        name,value=line.strip().split('=',1)
        cookies[name]=value
    kv={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
   #对输出结果定义一个变量
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url,kv,cookies)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
main()'''


#####################股票数据爬取##################################################################
'''import requests
from bs4 import BeautifulSoup
import re
import traceback
def getHTMLText(url, code='utf-8'):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        print('爬取失败')
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue
def getStockInfo(lst, stockURL, fpath):
    lst = list(set(lst))
    count = 0
    for stock in lst:
        url = stockURL + stock[-6:]
        html = getHTMLText(url)
        try:
            if html == '':
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-info'})
            name = stockInfo.find_all(attrs={'class': 'name'})[0]
            price = stockInfo.find_all(attrs={'class': 'latest'})[0]
            infoDict.update({'股票名称': name.text.split()[0], '最新行情': price.text.split()[0]})
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                ## 增加动态进度显示
                print('\r当前进度：{:.2f}%'.format(count * 100 / len(lst)), end='')    #'\r' 回车,回到当前行的行首,而不会换到下一行,如果接着输出的话,本行以前的内容会被逐一覆盖;'\n' 换行,就是输入完一行内容后,光标转到下一行的起始位置 ,不会回到行首。
        except:
            traceback.print_exc()
            continue
def main():
    stock_list_url = 'http://app.finance.ifeng.com/list/stock.php?t=ha'
    stock_info_url = 'https://www.laohu8.com/stock/'
    output_file = 'D:/BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)
main()'''
##############################################################################################3
import requests
import re
# 获取页面信息
def getHTMLText(url,kv,cookies):
    try:
        r = requests.get(url, headers=kv,cookies=cookies,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
# 解析页面
def parsePage(ilt, html):
    try:
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)    ##"raw_title":"南极人春装白色衬衫男长袖修身商务正装衬衣"
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)    ####"view_price":"59.00"
        nlt = re.findall(r'"nick":".*?"', html)           ####"nick":"南极人情豪专卖店"
        llt = re.findall(r'"item_loc":".*?"', html)        #####"item_loc":"浙江 金华"
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            name = eval(nlt[i].split(":")[1]).strip()
            loc = eval(llt[i].split(":")[1]).strip()
            ilt.append([price, title, name, loc])
    except:
        print("")
# 打印信息
def printGoodsList(ilt):
    tplt = "{:^4}\t{:^8}\t{:^15}\t{:^8}\t{:^26}"         ####这种用法属于Python的格式化输出字符：
                                          #######{0:^30}中的0是一个序号，表示格式化输出的第0个字符，依次累加；
                                        #######{0:^30}中的30表示输出宽度约束为30个字符；
                                        ###########{0:^30}中的^表示输出时居中对齐，若宽度小于字符串的实际宽度，以实际宽度输出；
    print(tplt.format("序号", "价格", "店名", "地区", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[2], g[3], g[1]))
def main():
    goods = '联想笔记本'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    coo='t=41653b20706345d12631aafb017b970f; cna=wKFrFnvBNRsCAXyATYJvStxu; thw=cn; v=0; cookie2=161c76018f25b9311c464719c2aa38ba; _tb_token_=e683b3559e733; unb=2212782603; uc3=lg2=UIHiLt3xD8xYTw%3D%3D&vt3=F8dByuqh437%2Fb%2FHhiE4%3D&id2=UUpgRKr%2BqoQHqA%3D%3D&nk2=pbJvuSGAeVW8Zg%3D%3D; csg=fa67ab25; lgc=%5Cu8D77%5Cu98CE%5Cu4E86%5Cu7A57%5Cu5B50; cookie17=UUpgRKr%2BqoQHqA%3D%3D; dnk=%5Cu8D77%5Cu98CE%5Cu4E86%5Cu7A57%5Cu5B50; skt=95221cd1c2aa6cc0; existShop=MTU3NzE2OTIzNA%3D%3D; uc4=nk4=0%40pwW3VMB6m4v7c%2B1Av8qXNXHpKjuL&id4=0%40U2gqy1t91FKKDK9ChmZT%2BdsbZc8w; tracknick=%5Cu8D77%5Cu98CE%5Cu4E86%5Cu7A57%5Cu5B50; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=%E5%AD%9032; _nk_=%5Cu8D77%5Cu98CE%5Cu4E86%5Cu7A57%5Cu5B50; cookie1=WvcYr4FuAHzJNq3CI7IDe0Vs2KH66XulIazTWuEHUKc%3D; enc=ZD%2B5tM4n0urXXyxYIdz7Z4LiPZNpca1RbpyqDcJbXdWrbo8pPCGUegPxhgUbAxO8z9dvygzlF3kQtcGOKB%2B%2FiA%3D%3D; mt=ci=91_1; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTbmhFo9Fy9aA%3D%3D&cookie15=W5iHLLyFOGW7aA%3D%3D; JSESSIONID=9AF926C20DC6A16E96A28DA11B9E3E84; l=cBP5-TLVq8T4HoOsBOCwourza77OSIRAguPzaNbMi_5CL6L66QbOoj_xYFp6VjWdTp8B4Ydbw2w9-etui-y06Pt-g3fP.; isg=BBYWvAMGVOBtyGOtf5Y7ZEB6Z8wYt1rxxS69T4B_AvmUQ7bd6EeqAXyx258Ka1IJreferer: https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
    cookies={}
    for line in coo.split(';'):
        name,value=line.strip().split('=',1)
        cookies[name]=value
    kv={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
   #对输出结果定义一个变量
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url,kv,cookies)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()





