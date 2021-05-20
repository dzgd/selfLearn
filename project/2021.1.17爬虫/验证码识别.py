'''
@Project ：project 
@File    ：验证码识别.py
@IDE     ：PyCharm 
@Author  ：青崖@一白鹿
@Date    ：2021/1/17 14:45 
'''

import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        # 此处是经过修改后的代码
        self.password = md5(password.encode("utf-8")).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()




from selenium import webdriver
from time import sleep
from PIL import Image
from selenium.webdriver import ActionChains
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
driver = webdriver.Chrome()
driver.get(url)

driver.maximize_window()
# save_screenshot的作用就是将当前页面进行截图保存
driver.save_screenshot('./古诗文网登陆界面.png')

#定位到验证码图片位置
img_tag = driver.find_elements_by_id('imgCode')[0]
# 获取验证码图片的左上角的坐标{'x': 764, 'y': 292},返回的是字典
loc = img_tag.location
# 获取验证码图片的高和宽{'height': 188, 'width': 300}，返回的是字典
size = img_tag.size
print(loc,size)
# 左上角坐标和右下角坐标
rangle = (int(loc['x']),int(loc['y']),int(loc['x']+size['width']),int(loc['y']+size['height']))
i = Image.open('./古诗文网登陆界面.png')
code_img_name = 'code_古诗文网验证码.png'
frame = i.crop(rangle)
frame.save(code_img_name)

userName_tag = driver.find_elements_by_id('email')[0]
password_tag = driver.find_elements_by_id('pwd')[0]
sleep(2)
userName_tag.send_keys('17828896385')
sleep(2)
password_tag.send_keys('dzg520118')
sleep(2)

chaojiying = Chaojiying_Client('duzhigao', 'dzg520118', '911827')	#用户中心>>软件ID 生成一个替换 96001
im = open('./code_古诗文网验证码.png', 'rb').read()								#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
result = chaojiying.PostPic(im, 1004)['pic_str']
print(result)

text_tag = driver.find_elements_by_id('code')[0]
text_tag.send_keys(result)

btn = driver.find_elements_by_id('denglu')[0]
btn.click()
sleep(2)
