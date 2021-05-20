import requests
from bs4 import BeautifulSoup
import traceback
# 异常处理
import xlwt


# 写入xls表
# Cookie记录登录信息，session请求
def get_content(url, headers=None, proxy=None):
    html = requests.get(url, headers=headers).content
    return html


def get_url(html):
    soup = BeautifulSoup(html, 'lxml')

    shop_url_list = soup.find_all('div', class_='tit')
    # class是关键字，所以不能直接用，class_就可以了
    # print (shop_url_list)
    # find是只查询一次，find_all()是查询多次返回一个列表，如果没有值就返回空
    # 列表推导式
    return [i.find('a')['href'] for i in shop_url_list]


def get_detail_content(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        price = soup.find('span', id='avgPriceTitle').text
        evaluation = soup.find('span', id='comment_score').find_all('span', class_='item')
        # 提取第一个span里面的title属性
        the_star = soup.find('div', class_='brief-info').find('span')['title']
        comments = soup.find('span', id="reviewCount").text
        title = soup.find('div', class_='breadcrumb').find('span').text
        address = soup.find('span', itemprop="street-address")['title']
        # u的意思是代表unicode编码
        print(u'店名:' + title)
        for i in evaluation:
            print(i.text)
        print(price)
        print(u'评价数量:' + comments)
        print(u'地址:' + address.strip())
        print(u'评价星级:' + the_star)
        print('===========================')
        return (title, evaluation[0].text, evaluation[1].text, evaluation[2].text, price, comments, address, the_star)
    except:
        traceback.print_exc()


if __name__ == '__main__':

    items = []
    all_url = []

    fk_url = []
    # 将所有商户的评论url全都打印出
    for i in range(0, 3):
        start_url = 'https://www.dianping.com/search/keyword/17/0_%E9%85%92%E5%BA%97/p' + str(i)
        all_url.append(start_url)

    base_url = 'https://www.dianping.com/'
    # 表头
    # 如果不设置cookie有可能导致出现403错误，禁止访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36' ,
        'Cookie': 'fspop=test; cy=17; cye=xian; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=177f7dba95dc8-005f474e0eb037-53e3566-100200-177f7dba95ec8; _lxsdk=177f7dba95dc8-005f474e0eb037-53e3566-100200-177f7dba95ec8; _hc.v=98fb828e-2923-5403-dc18-0b0e144f7db4.1614771104; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1614771105; s_ViewType=10; _dp.ac.v=cca643d9-5f63-4a66-811f-92ab60dcb21c; dplet=97098a89ebf6466d96eea05cb131b225; dper=52e1a0a2e55dde5b796e809e72c66e35dbe127e80793e4680bf02ed99015e09f0e2d5bd2da1aad516cd0b310810bf5cdb081c6f4a5e5198d83c911c16754b31f0b4c71a6252db2d00367e325ece2a87197187eaaed39aede563b2de3e352c7ff; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_9504504425; ctu=08eebc56af2eedae670f76f101f34391f2f07a494b517bfda8c82c3878192dfc; uamo=17828896385; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1614773388; _lxsdk_s=177f7dba95f-cf7-81b-80d%7C%7C446',

    }
    # 把多个列表里的url里面的url存储到一个列表里去，便于查询数据
    for url in all_url:
        start_html = get_content(url)
        durl = get_url(start_html)
        for i in durl:
            fk_url.append(i)
            print(i)

    # 列表推导式
    # base_url+url打印完整url
    url_list = [base_url + url for url in fk_url]

    for i in url_list:
        detail_html = get_content(i)
        item = get_detail_content(detail_html)
        items.append(item)

    newTable = 'DZDPdemo1.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('test1')
    headData = ['商户名字', '口味评分', '环境评分', '服务评分', '人均价格', '评论数量', '地址', '商户星级']
    for column in range(0, 8):
        # 0把行定位到第一行了列 后面是设置字体
        ws.write(0, column, headData[column], xlwt.easyxf('font:bold on'))

    index = 1

    lens = len(items)
    print(u'数据总长度=' + str(lens))
    # 有多少数据
    # 只对列做了一个for循环，因为行列都要写入，所以做两个for循环
    # 多少行由列表数据决定的，有多少数据就有多少行
    # index代表的是行，我们从1开始是因为标题已经占据了第一行
    # 对list做了两次索引，第一次是商户信息拿出来，第二个索引是把商户的详细信息拿出来
    # 简单的来说，j就代表一个商户，i[0]相当于代表店名，i[1]相当于代表evaluation[0].text依次类推
    for j in range(0, lens):
        for i in range(0, 8):
            ws.write(index, i, items[j][i])
        index += 1
    wb.save(newTable)
