'''import urllib.request
url="http://127.0.0.1:5000/"
r=urllib.request.urlopen(url)
data=r.read()
html=data.decode()
print(html)




##################   GET请求   ############
import urllib.request
import urllib.parse
url='http://www.baidu.com/s?wd='
key='fengxin的博客'
key_code=urllib.request.quote(key)      #因为URL里含中文，需要进行编码
url_all=url+key_code
header={
    'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}   #头部信息
request=urllib.request.Request(url_all,headers=header)
reponse=urllib.request.urlopen(request).read()
fh=open("./baidu.html","wb")    #写入文件中
fh.write(reponse)
fh.close()



##################      POST请求     ##################
import urllib.request
import urllib.parse
url='http://www.iqianyue.com/mypost'
header={
   'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

data={'name':'fengxin','pass':'123'}
postdata=urllib.parse.urlencode(data).encode('utf8') #进行编码
request=urllib.request.Request(url,postdata)
reponse=urllib.request.urlopen(request).read()

fhandle=open("./1.html","wb")
fhandle.write(reponse)
fhandle.close()'''


