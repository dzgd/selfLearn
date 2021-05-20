import requests
from bs4 import BeautifulSoup
import urllib.parse

import xlwt
import xlrd

# 账号密码
def login(username, password):
    url = 'https://accounts.douban.com/j/mobile/login/basic'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
        'Origin': 'https://accounts.douban.com',
        'content-Type': 'application/x-www-form-urlencoded',
        'x-requested-with': 'XMLHttpRequest',
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'connection': 'keep-alive'
        , 'Host': 'accounts.douban.com'
    }
    # 登陆需要携带的参数
    data = {
        'name': '',
        'password': '',
        'remember': 'false',
    }
    data['name'] = username
    data['password'] = password
    data = urllib.parse.urlencode(data)
    print(data)
    req = requests.post(url, headers=header, data=data)
    cookies = requests.utils.dict_from_cookiejar(req.cookies)
    print(cookies)
    return cookies

def getcomment(cookies, mvid):  # 参数为登录成功的cookies(后台可通过cookies识别用户，电影的id)
    start = 0
    w = xlwt.Workbook(encoding='utf-8')  # #创建可写的workbook对象
    ws = w.add_sheet('sheet1')  # 创建工作表sheet
    index = 0  # 表示行的意思，在xls文件中写入对应的行数
    ws.write(index, 0, "序号")  # 第index行，第0列写入 index
    ws.write(index, 1, "评论者")  # 第index行，第1列写入 评论者
    ws.write(index, 2, "评星")  # 第index行，第2列写入 评星
    ws.write(index, 3, "投票数")  # 第index行，第3列写入 投票数
    ws.write(index, 4, "评论内容")  # 第index行，第4列写入 评论内容
    index = 1
    while True:
        # 模拟浏览器头发送请求
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }
        # try catch 尝试，一旦有错误说明执行完成，没错误继续进行
        try:
            # 拼凑url 每次star加20
            url = 'https://movie.douban.com/subject/' + str(mvid) + '/comments?start=' + str(start) + '&limit=20&sort=new_score&status=P&comments_only=1'
            start += 20
            # 发送请求
            req = requests.get(url, cookies=cookies, headers=header)
            # 返回的结果是个json字符串 通过req.json()方法获取数据
            res = req.json()
            res = res['html']  # 需要的数据在`html`键下
            soup = BeautifulSoup(res, 'lxml')  # 把这个结构化html创建一个BeautifulSoup对象用来提取信息
            node = soup.select('.comment-item')  # 每组class 均为comment-item  这样分成20条记录(每个url有20个评论)
            for va in node:  # 遍历评论
                name = va.a.get('title')  # 获取评论者名称
                star = va.select_one('.comment-info').select('span')[1].get('class')[0][-2]  # 星数好评
                votes = va.select_one('.votes').text  # 投票数
                comment = va.select_one('.short').text  # 评论文本
                print(name, star, votes, comment)
                ws.write(index, 0, index)  # 第index行，第0列写入 index
                ws.write(index, 1, name)  # 第index行，第1列写入 评论者
                ws.write(index, 2, star)  # 第index行，第2列写入 评星
                ws.write(index, 3, votes)  # 第index行，第3列写入 投票数
                ws.write(index, 4, comment)  # 第index行，第4列写入 评论内容
                index += 1
        except Exception as e:  # 有异常退出
            print(e)
            break
    w.save('test.xls')  # 保存为test.xls文件


if __name__ == '__main__':
    username = input('输入账号：')  #17828896385
    password = input('输入密码：')    #dzg520118
    cookies = login(username, password)
    mvid = input('电影的id为：')   #25907124:姜子牙
    getcomment(cookies, mvid)