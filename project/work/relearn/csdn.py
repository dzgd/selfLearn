'''
@Project ：project 
@File    ：csdn.py
@IDE     ：PyCharm 
@Author  ：青崖@一白鹿
@Date    ：2020/12/25 19:25 
'''

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.csdn.net/nav/python')

#下拉若干次
for i in range(5):
     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
     time.sleep(1)

#定位所有链接
blog_url = driver.find_elements_by_css_selector('div.title > h2 > a') #注意:这里保存的是所有element对象
print(blog_url)
