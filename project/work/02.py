import requests
from lxml import etree
url = "https://www.pearvideo.com/video_1715023"
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}

res = requests.get(url = url,headers=header).text
tree = etree.HTML(res)
link = tree.xpath('//div[@id="poster"]/@data-cid')[0]
h = tree.xpath('//div[@id="poster"]/img/@src')[0].split("/")[-1][:-6]
new = "https://video.pearvideo.com/mp4/third/20210105/cont-"+link+"-"+h+"-hd.mp4"
print(new)

