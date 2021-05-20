import time
from selenium import webdriver
import pymysql
source_url="https://www.icourse163.org/channel/2001.htm"

class mooc():
    def start(self):
        self.driver = webdriver.Chrome()
        self.driver.get(source_url)
        self.driver.maximize_window()

    def createtable(self):
        try:
            self.cursor.execute("drop table mooc")
        except:
            pass
        self.cursor.execute('create table mooc(id int,cCourse varchar(32),cTeacher varchar(16),cTeam varchar(64),cCollage varchar(32),cProcess varchar(64),' \
      'cCount varchar(64),cBrief text);')

    def connect(self):
        self.con = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="dujin",
                                   charset="utf8")
        self.cursor = self.con.cursor(pymysql.cursors.DictCursor)
        opened = True
        self.count = 0

    def close(self):
        self.con.commit()
        self.con.close()

    def mo(self):
        time.sleep(1)
        block = self.driver.find_element_by_xpath("//div[@class='_1gBJC']")
        lis = block.find_elements_by_xpath("./div/div[@class='_3KiL7']")
        for li in lis:
            l=li.text.split("\n")
            if l[0]!="国家精品":
                l=["1"]+l
            print(l[0],l[1],l[2],l[3],l[4],l[5])
            self.count+=1
            cCourse=l[1]
            cCollage=l[2]
            cTeacher=l[3]
            cCount=l[4]
            li.click()
            window = self.driver.window_handles
            # 切换到新页面
            self.driver.switch_to.window(window[1])
            time.sleep(1)
            cBrief=self.driver.find_element_by_xpath("//div[@id='j-rectxt2']").text
            cTeam=self.driver.find_element_by_xpath("//*[@id='course-enroll-info']/div/div[1]/div[2]/div[1]/span[2]").text
            team=self.driver.find_element_by_xpath("//*[@id='j-teacher']/div/div/div[2]/div/div[@class='um-list-slider_con']").text.split("\n")
            no=len(team)
            cProcess=""
            for i in range(0,no):
                if (i%2==0)&(i!=0):
                    cProcess=cProcess+"/"+team[i]
                elif (i%2==0):
                    cProcess=cProcess+team[i]
            print(cProcess)
            self.cursor.execute("insert into mooc(id, cCourse, cTeacher, cTeam, cCollage, cProcess, cCount, cBrief) "
                           "values( % s, % s, % s, % s, % s, % s, % s, % s)",
                           (self.count, cCourse, cTeacher, cTeam, cCollage, cProcess, cCount, cBrief))
            self.driver.close()
            self.driver.switch_to.window(window[0])
            time.sleep(1)
            #cProcess=
        time.sleep(1)
        if (self.driver.find_elements_by_xpath('//a[@class="_3YiUU "]')[-1].text == '下一页') & (self.count<=30):
            next = self.driver.find_elements_by_xpath('//a[@class="_3YiUU "]')[-1]
            next.click()
            self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
            self.mo()
c=mooc()
c.start()
c.connect()
c.createtable()
time.sleep(3)
c.mo()
c.close()

#心得体会：翻页后出现无法点击的情况，请教同学后知道是因为点击下一页后，页面在下面，因为某种原因，要将页面拉至上方才能继续：使用"window.scrollTo(document.body.scrollHeight,0)"
#同时所爬取mooc该网站上一页与下一页的可点击/不可点击时的tag一样，添加了一些判断解决。