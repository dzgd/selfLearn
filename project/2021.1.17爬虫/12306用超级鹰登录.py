'''
@Project ：project 
@File    ：12306用超级鹰登录.py
@IDE     ：PyCharm 
@Author  ：青崖@一白鹿
@Date    ：2021/1/17 21:53 
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
driver = webdriver.Chrome()
url = 'https://kyfw.12306.cn/otn/resources/login.html'
driver.get(url)
driver.maximize_window()
a_tag = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')[0]
a_tag.click()
# save_screenshot的作用就是将当前页面进行截图保存
driver.save_screenshot('./12306.png')

#定位到验证码图片位置
img_tag = driver.find_elements_by_id('J-loginImg')[0]
# 获取验证码图片的左上角的坐标{'x': 764, 'y': 292},返回的是字典
loc = img_tag.location
# 获取验证码图片的高和宽{'height': 188, 'width': 300}，返回的是字典
size = img_tag.size
print(loc,size)
# 左上角坐标和右下角坐标
rangle = (int(loc['x']),int(loc['y']),int(loc['x']+size['width']),int(loc['y']+size['height']))
i = Image.open('./12306.png')
code_img_name = 'code.png'
frame = i.crop(rangle)
frame.save(code_img_name)

userName_tag = driver.find_elements_by_id('J-userName')[0]
password_tag = driver.find_elements_by_id('J-password')[0]
sleep(2)
userName_tag.send_keys('17828896385')
sleep(2)
password_tag.send_keys('dzg520118')
sleep(2)

chaojiying = Chaojiying_Client('duzhigao', 'dzg520118', '911827')	#用户中心>>软件ID 生成一个替换 96001
im = open('./code.png', 'rb').read()								#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
result = chaojiying.PostPic(im, 9004)['pic_str']
all_list = []
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
print(all_list)
for i in all_list:
    x = i[0]
    y = i[1]
    ActionChains(driver).move_to_element_with_offset(img_tag,x,y).click().perform()


btn = driver.find_elements_by_id('J-login')[0]
btn.click()
sleep(2)
