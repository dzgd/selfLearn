import scrapy
from selenium import webdriver

name = 'doubanSpider'
current_url = 'https://movie.douban.com/top250/'
try:
    print('start')
    driver = webdriver.Chrome()
    driver.get(current_url)
    html = driver.page_source
    print(html)
    print("beginning")
    lis = html.css('.info')
    print(lis)
    for li in lis:
        # 利用CSS选择器获取信息
        name = li.css('.hd span::text').extract()
        title = ''.join(name)
        info = li.css('p::text').extract()[1].replace('\n', '').strip()
        score = li.css('.rating_num::text').extract_first()
        people = li.css('.star span::text').extract()[1]
        words = li.css('.inq::text').extract_first()
        print(title)
        # 生成字典
except Exception as err:
    print(err)


