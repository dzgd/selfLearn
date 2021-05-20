
next_page_url = "http://www.dianping.com/shop/l7dKOYLSvg2ouBvr/review_all/p2"
a = next_page_url.split(".")[2].split("/")
b = "p" + str(int(a[-1][1])+1)
next_page_url = "http://www.dianping.com/shop/l7dKOYLSvg2ouBvr/review_all/" + b
print(next_page_url)