'''
@Project ：project 
@File    ：boss_selenium爬取.py
@IDE     ：PyCharm 
@Author  ：青崖@一白鹿
@Date    ：2021/1/19 12:06 
'''

from selenium import webdriver
from time import sleep
url = 'https://www.zhipin.com/xian/'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
in_text_tag = driver.find_elements_by_class_name('ipt-search')[0]
sleep(2)
in_text_tag.send_keys('python')
btn = driver.find_elements_by_xpath('//*[@id="wrap"]/div[3]/div/div/div[1]/form/button')[0]
btn.click()
sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight*0.05)")
sleep(5)
li_list = driver.find_elements_by_xpath('//*[@id="main"]/div/div[3]/ul/li')
for li in li_list:
    detail_url = 'https://www.zhipin.com' + li.find_elements_by_xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a')[0].get_attribute('href')
    address = li.find_elements_by_xpath('./div/div[1]/div[1]/div/div[1]/span[2]/span')[0].text
    # salary = li.find_elements_by_xpath('./div/div[1]/div[1]/div/div[1]/span[2]/span[@red]').text.strip()
    # school = li.find_elements_by_xpath('./div/div[1]/div[1]/div/div[2]/p').text.strip()
    # names = li.find_elements_by_xpath('./div/div[1]/div[1]/div/div[2]/div/h3').text.strip()
    # with open('./BOSS直聘爬取.txt','w',encoding='utf-8') as fp:
    #     fp.write(detail_url + '\n' + address + '\n' + salary + '\n' + school +'\n' +names +'\\n')
print('over!!!!')
print(detail_url)
print(address)


