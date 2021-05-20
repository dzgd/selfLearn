import scrapy
from selenium import webdriver
from ..items import populationItem
import time


class populationInfo(scrapy.Spider):
    name = "populationInfo"
    current_url = 'https://cl.rkpc.stats.gov.cn/clv1/dataquery/custom/FlexibleSearch'

    def start_requests(self):
        url = populationInfo.current_url
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
            print('1')
            #print(response.url)
            self.driver = webdriver.Chrome()
            print(populationInfo.current_url)
            self.driver.get(populationInfo.current_url)
            self.count = 0
            js = "window.scrollBy(0,document.body.scrollHeight*0.5)"
            self.driver.execute_script(js)
            time.sleep(2)
            # html = driver.page_source
            # print(html)
            if self.count ==0:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                lis = self.driver.find_elements_by_xpath("//table[@class='ant-table-fixed']/tbody/tr")
                for li in lis:
                    lists = li.text.split(" ")
                    item = populationItem()
                    item["id"] = lists[0]
                    item["code"] = lists[5]
                    item["name"] = lists[9]
                    item["relation"] = lists[10]
                    item["shenfenzhenghaoma"] = lists[11]
                    yield item
            for i in range(10):
                self.count = i + 1
                #if (self.driver.find_elements_by_xpath('//a[@class="next paginate_button"]')[-1].text == '下一页') & (self.count <= 5):
                next = self.driver.find_elements_by_xpath('//li[@class="ant-pagination-next"]')
                #/a[@class="ant-pagination-item-link"
                next.click()
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                js = "window.scrollBy(0,document.body.scrollHeight*0.5)"
                self.driver.execute_script(js)
                time.sleep(2)
                print(self.driver.current_url)
                time.sleep(2)
                lis = self.driver.find_elements_by_xpath("//table[@class='ant-table-fixed']/tbody/tr")
                for li in lis:
                    lists = li.text.split(" ")
                    item = populationItem()
                    item["id"] = lists[0]
                    item["code"] = lists[5]
                    item["name"] = lists[9]
                    item["relation"] = lists[10]
                    item["shenfenzhenghaoma"] = lists[11]
                    yield item
            print("一共爬取{}页的数据".format(self.count))
            self.driver.close()
        except Exception as err:
            print(err)