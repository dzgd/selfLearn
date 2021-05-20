from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
url = 'https://www.dianping.com/'
chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
time.sleep(5)
s = driver.find_element_by_xpath('/html/body/div[1]/div[1]').click()
p = driver.find_element_by_xpath('//*[@id="top-nav"]/div/div[2]/span[1]/a[1]').click()
time.sleep(1)
js = "window.scrollBy(0,document.body.scrollHeight*0.2)"
driver.execute_script(js)
time.sleep(2)
js = "window.scrollBy(0,document.body.scrollHeight*0.5)"
driver.execute_script(js)
time.sleep(2)
js = "window.scrollBy(document.body.scrollHeight*0.7,0)"
driver.execute_script(js)
time.sleep(2)
url = 'https://account.dianping.com/account/iframeLogin?callback=EasyLogin_frame_callback0&amp;wide=false&amp;protocol=https:&amp;redir=https%3A%2F%2Fwww.dianping.com'
driver.get(url)
page = driver.page_source
q = driver.find_element_by_xpath('/html/body/div/div[2]/div[5]/span').click()
time.sleep(1)
w = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[1]/div[1]/span[2]').click()
user = driver.find_element_by_id("account-textbox")
pwd = driver.find_element_by_id("password-textbox")
login = driver.find_element_by_id("login-button-account")
time.sleep(1)
user.send_keys("18597808159")
time.sleep(1)
pwd.send_keys("duzhigaoyangxiuzhen520118")
login.click()
time.sleep(1)
button = driver.find_element_by_id('yodaBox')
move_x_offset = driver.find_element_by_id('yodaBoxWrapper').size['width']
webdriver.ActionChains(driver).drag_and_drop_by_offset(
    button, move_x_offset, 0).perform()
