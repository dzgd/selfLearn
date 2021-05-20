import scrapy
from selenium import webdriver
from ..items import lineItem
import time


class shareSpider(scrapy.Spider):
    name = "shareSpider"
    current_url = 'http://quote.eastmoney.com/center/gridlist.html#hs_a_board'

    def start_requests(self):
        url = shareSpider.current_url
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
            print('1')
            print(response.url)
            self.driver = webdriver.Chrome()
            self.driver.get(response.url)
            self.count = 0
            js = "window.scrollBy(0,document.body.scrollHeight*0.5)"
            self.driver.execute_script(js)
            time.sleep(2)
            # html = driver.page_source
            # print(html)
            if self.count ==0:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                lis = self.driver.find_elements_by_xpath("//*[@id='table_wrapper-table']/tbody/tr")
                for li in lis:
                    lists = li.text.split(" ")
                    item = lineItem()
                    item["id"] = lists[1]
                    item["name"] = lists[2]
                    item["new_price"] = lists[6]
                    item["up_rate"] = lists[7]
                    item["down_rate"] = lists[8]
                    item["pass_number"] = lists[9]
                    item["pass_money"] = lists[10]
                    item["rate"] = lists[11]
                    item["highest"] = lists[12]
                    item["lowest"] = lists[13]
                    item["today"] = lists[14]
                    item["yesterday"] = lists[15]
                    yield item
            for i in range(10):
                self.count = i + 1
                #if (self.driver.find_elements_by_xpath('//a[@class="next paginate_button"]')[-1].text == '下一页') & (self.count <= 5):
                next = self.driver.find_elements_by_xpath('//a[@class="next paginate_button"]')[-1]
                next.click()
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                js = "window.scrollBy(0,document.body.scrollHeight*0.5)"
                self.driver.execute_script(js)
                time.sleep(2)
                print(self.driver.current_url)
                time.sleep(2)
                lis = self.driver.find_elements_by_xpath("//*[@id='table_wrapper-table']/tbody/tr")
                for li in lis:
                    lists = li.text.split(" ")
                    item = lineItem()
                    item["id"] = lists[1]
                    item["name"] = lists[2]
                    item["new_price"] = lists[6]
                    item["up_rate"] = lists[7]
                    item["down_rate"] = lists[8]
                    item["pass_number"] = lists[9]
                    item["pass_money"] = lists[10]
                    item["rate"] = lists[11]
                    item["highest"] = lists[12]
                    item["lowest"] = lists[13]
                    item["today"] = lists[14]
                    item["yesterday"] = lists[15]
                    yield item
            print("一共爬取{}页的股市数据".format(self.count))
            self.driver.close()
        except Exception as err:
            print(err)