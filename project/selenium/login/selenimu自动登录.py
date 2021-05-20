from selenium import webdriver
import time
try:

    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000")
    user = driver.find_element_by_name("user")
    pwd = driver.find_element_by_name("pwd")
    login = driver.find_element_by_name("login")
    time.sleep(0.5)
    user.send_keys("xxx")
    time.sleep(0.5)
    pwd.send_keys("123")
    login.click()
    time.sleep(5)
except Exception as err:
    print(err)





#####selenimu实现自动登录并爬取数据
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
# def login():
#     print(driver.current_url)
#     user = driver.find_element_by_name("user")
#     pwd = driver.find_element_by_name("pwd")
#     login = driver.find_element_by_name("login")
#     user.send_keys("xxx")
#     pwd.send_keys("123")
#     login.click()
#     time.sleep(0.5)
#
# def spider():
#     print(driver.current_url)
#     trs=driver.find_elements_by_tag_name("tr")
#     for i in range(1,len(trs)):
#         tds =trs[i].find_elements_by_tag_name("td")
#         if len(tds)==3:
#             mark = tds[0].text
#             model=tds[1].text
#             price=tds[2].text
#             print("%-16s%-16s%-16s" %(mark,model,price))
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)  #chrome_options=chrome_options
# try:
#     driver.get("http://127.0.0.1:5000")
#     login()
#     spider()
# except Exception as err:
#     print(err)
# driver.close()
