from selenium import webdriver
import pymysql
from selenium.webdriver.common.keys import Keys
import time
class MySpider:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}

    imagePath = "download"

    def startUp(self, url, key):
        # Initializing Chrome browser
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome()  #chrome_options=chrome_options
        # Initializing variables
        self.No = 0
        self.driver.get(url)
        keyInput = self.driver.find_element_by_id("key")
        keyInput.send_keys(key)
        keyInput.send_keys(Keys.ENTER)
        self.con = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="dujin",
                              charset="utf8")
        self.cursor = self.con.cursor()
        try:
            self.cursor.execute("drop table phones007")
        except:
            pass
        self.cursor.execute("create table phones007 (mNo  varchar(32) primary key, mMark varchar(256),mPrice varchar(32),mNote varchar(1024))")
    def processSpider(self):
        try:
            print(self.driver.current_url)
            self.driver.maximize_window()
            # 纵向滚动条通过scrollBy坐标来滚动
            js = "window.scrollBy(0,document.body.scrollHeight*0.3)"
            self.driver.execute_script(js)
            time.sleep(3)
            js = "window.scrollBy(0,document.body.scrollHeight*0.5)"
            self.driver.execute_script(js)
            time.sleep(3)
            js = "window.scrollBy(0,document.body.scrollHeight*0.7)"
            self.driver.execute_script(js)
            time.sleep(3)
            js = "window.scrollBy(0,document.body.scrollHeight*0.8)"
            self.driver.execute_script(js)
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            lis = self.driver.find_elements_by_xpath("//div[@id='J_goodsList']//li[@class='gl-item']")
            no = 0
            print(len(lis))
            for li in lis:
                no += 1
                try:
                    price = li.find_element_by_xpath(".//div[@class='p-price']//i").text
                except:
                    price = "0"
                try:
                    note = li.find_element_by_xpath(".//div[@class='p-name p-name-type-2']//em").text
                    mark = note.split(" ")[0]
                    mark = mark.replace("爱心东东\n", "")
                    mark = mark.replace(",", "")
                    note = note.replace("爱心东东\n", "")
                    note = note.replace(",", "")
                except:
                    note = ""
                    mark = ""
                print(no, mark, price,note)
                self.cursor.execute(
                "insert into phones007 (mNo,mMark,mPrice,mNote) values (%s,%s,%s,%s)",
                (no, mark, price,note))
                self.con.commit()
                time.sleep(2)
                if no >= 50:
                    return
            self.con.close()
        except Exception as err:
             print(err)
url = "http://www.jd.com"
spider = MySpider()
spider.startUp(url, "手机")
spider.processSpider()

