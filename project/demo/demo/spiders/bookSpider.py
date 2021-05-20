import scrapy
from bs4 import UnicodeDammit

from ..items import BookItem


class bookSpider(scrapy.Spider):
    name = "bookSpider"
    key = 'python'
    source_url = 'http://search.dangdang.com/'

    def start_requests(self):
        url = bookSpider.source_url + "?key=" + bookSpider.key
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
            dammit = UnicodeDammit(response.body, ["utf-8", "gbk"])
            data = dammit.unicode_markup
            selector = scrapy.Selector(text=data)
            lis = selector.xpath("//li['@ddt-pit'][starts-with(@class,'line')]")
            for li in lis:
                title = li.xpath("./a[position()=1]/@title").extract_first()
                price = li.xpath("./p[@class='price']/span[@class='search_now_price']/text()").extract_first()
                author = li.xpath("./p[@class='search_book_author']/span[position()=1]/a/@title").extract_first()
                date = li.xpath("./p[@class='search_book_author']/span[position()=last()- 1]/text()").extract_first()
                publisher = li.xpath(
                    "./p[@class='search_book_author']/span[position()=last()]/a/@title ").extract_first()
                detail = li.xpath("./p[@class='detail']/text()").extract_first()
                # detail有时没有，结果None
                item = BookItem()
                item["title"] = title.strip() if title else ""
                item["author"] = author.strip() if author else ""
                item["date"] = date.strip()[1:] if date else ""
                item["publisher"] = publisher.strip() if publisher else ""
                item["price"] = price.strip() if price else ""
                item["detail"] = detail.strip() if detail else ""
                yield item
            # link = selector.xpath("//div[@class='paging']/ul[@name='Fy']/li[@class='next'] / a / @ href").extract_first()
            # if link:
            #     url = response.urljoin(link)
            #     yield scrapy.Request(url=url, callback=self.parse)

        except Exception as err:
            print(err)