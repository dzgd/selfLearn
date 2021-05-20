'''
@Project ：project 
@File    ：QQ空间爬取.py
@IDE     ：PyCharm 
@Author  ：青崖@一白鹿
@Date    ：2021/1/17 19:05 
'''


from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("https://qzone.qq.com/")
driver.switch_to.frame('login_frame')
a_tag = driver.find_element_by_id('switcher_plogin')
a_tag.click()

userName_tag = driver.find_element_by_id("u")
password_tag = driver.find_element_by_id('p')
sleep(1)
userName_tag.send_keys('1909889038')
password_tag.send_keys('dzg52011888')
sleep(1)
btn = driver.find_element_by_id('login_button')
btn.click()
sleep(3)
driver.quit()