from scrapy import cmdline
cmdline.execute("scrapy crawl bookSpider -s LOG_ENABLED=False".split())
