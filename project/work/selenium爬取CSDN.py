from selenium import webdriver
import os
os.chdir(r'E:\data\爬取CSDN')

import time
import pandas as pd

def scroll_down(driver,num):
    for i in range(num):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(1)

def save_data(df):
    data=pd.DataFrame(df,columns=['blog_name','code_time','blog_num',
                                'view_num','fans_num','likes_num',
                                'comments_num','collections_num'])
    data.to_csv('csdn_user.csv',index=False,encoding='gb18030')

def crawler_csdn(parts_list):
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('excludeSwitches',['enable-automation'])
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    opt.add_argument('blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(options=opt)
    df = []
    for part in parts_list:
        count=0
        url_des='https://www.csdn.net/nav/'+part
        driver.get(url_des)
        scroll_down(driver,30)
        time.sleep(2)
        print('开始爬取{}部分'.format(part))
        blog_list=[]
        blog_url = driver.find_elements_by_css_selector('div.title > h2 > a')
        for url in blog_url:
            blog_list.append(url.get_attribute('href'))
        print('共{}个博主'.format(len(blog_list)))
        for i in range(len(blog_list)):
            try:
                driver.get(blog_list[i])
                blog_name = driver.find_element_by_css_selector('div.profile-intro-name-boxTop > a >span.name').text
                code_time = driver.find_element_by_css_selector('span.personal-home-page.personal-home-years').text
                blog_num = driver.find_element_by_css_selector(
                    'div.data-info.d-flex.item-tiling>dl.text-center>a>dt>span.count').text
                inf_list = driver.find_elements_by_css_selector('div.data-info.d-flex.item-tiling>dl.text-center>dt>span.count')
                df.append([blog_name, code_time, blog_num,
                           inf_list[0].text, inf_list[1].text, inf_list[2].text,
                           inf_list[3].text, inf_list[4].text])
                count += 1
                print('第{}个博主信息爬取完成'.format(count))
            except:
                print('相关信息不全')
        print('{}部分爬取完成'.format(part))
    return df


if __name__ =='__main__':
    start = time.time()
    parts_list=['Python']
    #parts_list=['Python','Java','web','arch','db']
    df = crawler_csdn(parts_list)
    save_data(df)
    end = time.time()
    spend_time = int((end-start)/60)
    print('共花费{}分钟'.format(spend_time))