from bs4 import BeautifulSoup
import pymysql

try:
    con = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="dujin",
                          charset="utf8")
    cursor = con.cursor()
    try:
        cursor.execute("drop table population01")
    except:
        pass
    try:
        sql = "create table population01(id int(16) primary key,code varchar(256),name01 varchar(256),relation varchar(256),shenfenzhenghaoma varchar(256))"
        cursor.execute(sql)
    except:
        cursor.execute("delete from population01")
except Exception as err:
    print(err)
doc1 = '''<tr class="ant-table-row ant-table-row-level-0" data-row-key="1305749989670531073_1604214874430002"><td><span class="ant-table-row-indent indent-level-0" style="padding-left: 0px;"></span><!---->1</td><td>610102002010</td><td>610102709000</td><td>-</td><td>610102002010001</td><td>610102002010001001</td><td>普通住户</td><td>普查员登记</td><td>1</td><td>张欣</td><td>户主</td><td>******197709******</td><td>-</td><td>男</td><td>1977</td><td>9</td><td>汉族</td><td>本普查小区</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>其他县（市、区、旗）</td><td>610116</td><td>陕西省</td><td>西安市</td><td>长安区</td><td></td><td></td><td></td><td></td><td>十年以上</td><td>随同离开/投亲靠友</td><td>大学本科</td><td>是</td><td>43</td><td>-</td></tr>'''
doc2 = '''<tr class="ant-table-row ant-table-row-level-0" data-row-key="1305749989670531073_1604215444503010"><td><span class="ant-table-row-indent indent-level-0" style="padding-left: 0px;"></span><!---->5</td><td>610102002010</td><td>610102709000</td><td>-</td><td>610102002010001</td><td>610102002010001008</td><td>普通住户</td><td>普查员登记</td><td>2</td><td>柏志杰</td><td>配偶</td><td>******194106******</td><td>-</td><td>男</td><td>1941</td><td>6</td><td>汉族</td><td>本普查小区</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>本村（居）委会</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>没有离开户口登记地</td><td>-</td><td>初中</td><td>是</td><td>79</td><td>-</td></tr>'''
doc3 = '''<tr class="ant-table-row ant-table-row-level-0" data-row-key="1305749989670531073_1604215697642018"><td><span class="ant-table-row-indent indent-level-0" style="padding-left: 0px;"></span><!---->8</td><td>610102002010</td><td>610102709000</td><td>-</td><td>610102002010001</td><td>610102002010001016</td><td>普通住户</td><td>普查员登记</td><td>3</td><td>郭宁</td><td>孙子女</td><td>******199510******</td><td>-</td><td>男</td><td>1995</td><td>10</td><td>汉族</td><td>本普查小区</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>本村（居）委会</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>没有离开户口登记地</td><td>-</td><td>高中</td><td>是</td><td>25</td><td>-</td></tr>'''
doc4 = '''<tr class="ant-table-row ant-table-row-level-0" data-row-key="1305749989670531073_1604217514300041"><td><span class="ant-table-row-indent indent-level-0" style="padding-left: 0px;"></span><!---->12</td><td>610102002010</td><td>610102709000</td><td>-</td><td>610102002010001</td><td>610102002010001026</td><td>普通住户</td><td>普查员登记</td><td>2</td><td>李赟景</td><td>子女</td><td>******200410******</td><td>-</td><td>女</td><td>2004</td><td>10</td><td>汉族</td><td>本普查小区</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>其他县（市、区、旗）</td><td>610112</td><td>陕西省</td><td>西安市</td><td>未央区</td><td></td><td></td><td></td><td></td><td>二年以上，不满三年</td><td>学习培训</td><td>高中</td><td>是</td><td>16</td><td>-</td></tr>'''
doc5 = '''<tr class="ant-table-row ant-table-row-level-0" data-row-key="1305749989670531073_1604217514329042"><td><span class="ant-table-row-indent indent-level-0" style="padding-left: 0px;"></span><!---->13</td><td>610102002010</td><td>610102709000</td><td>-</td><td>610102002010001</td><td>610102002010001026</td><td>普通住户</td><td>普查员登记</td><td>3</td><td>李赟泽</td><td>子女</td><td>******201212******</td><td>-</td><td>男</td><td>2012</td><td>12</td><td>汉族</td><td>本普查小区</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>其他县（市、区、旗）</td><td>610112</td><td>陕西省</td><td>西安市</td><td>未央区</td><td></td><td></td><td></td><td></td><td>二年以上，不满三年</td><td>学习培训</td><td>小学</td><td>-</td><td>7</td><td>-</td></tr>'''
docs = [doc1,doc2,doc3,doc4,doc5]
for doc in docs:
    soup = BeautifulSoup(doc,"lxml")
    #s = soup.prettify()
    #print(s)
    tags = soup.find_all("td")
    a = []
    for tag in tags:
        if tag.text:
            if tag.text !="-":
                a.append(tag.text)
    print(a[0],a[4],a[8],a[9],a[10])
    cursor.execute(
        "insert into population01(id,code,name01,relation,shenfenzhenghaoma)values (%s,%s,%s,%s,%s)",(a[0],a[4],a[8],a[9],a[10]))
    con.commit()
print("sucessefully")
