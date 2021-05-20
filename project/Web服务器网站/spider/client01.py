import urllib.request
import re
import sqlite3
def searchWeb(html):
    rows=[]
    #查询第一个<tr>...</tr>行
    m=re.search(r"<tr>",html)
    n=re.search(r"</tr>",html)
    if m!=None and n!=None:
    #跳过第一行的标题
        html=html[n.end():]
    # 查询第二行开始的数据部分
    m=re.search(r"<tr>",html)
    n=re.search(r"</tr>",html)
    while(m!=None and n!=None):
        row=[]
        #start 是<tr>的结束位置
        start=m.end()
        #end 是</tr>的开始位置
        end=n.start()
        #t 是<tr>...</tr>包含的字符串
        t=html[start:end]
        #html[n.end():]是剩余的 html
        html=html[n.end():]
        #查询第一组<td>...</td>
        a=re.search(r"<td>",t)
        b=re.search(r"</td>",t)
        i=0
        while (a!=None and b!=None):
            start=a.end()
            end=b.start()
            #找到一组<td>...</td>的数据
            row.append(t[start:end])
            #t[b.end():]是本行剩余的部分
            t = t[b.end():]
            a = re.search(r"<td>", t)
            b = re.search(r"</td>", t)
        #增加一行数据
        rows.append(row)
#继续查找下一行<tr>...</tr>
        m = re.search(r"<tr>", html)
        n = re.search(r"</tr>", html)
    return rows
def saveDB(rows):
    if len(rows)==0:
    #没有数据就返回
        return
    try:
        con = sqlite3.connect("students.db")
        cursor = con.cursor()
        try:
            #如果有 students 表就删除
            cursor.execute("drop table students")
        except:
            pass
        try:
        #建立新的 students 表
            sql = "create table students (No varchar(128) primary key,Name varchar(128),Gender varchar(128),Age int)"
            cursor.execute(sql)
        except:
            pass
        for row in rows:
            if(len(row)==4):
                #插入一条记录
                sql="insert into students (No,Name,Gender,Age) values (?,?,?,?)"
                try:
                    No=row[0]
                    Name=row[1]
                    Gender=row[2]
                    Age=int(row[3])
                    cursor.execute(sql,(No,Name,Gender,Age))
                except Exception as err:
                    print(err)
            #数据库提交保存
        con.commit()
        con.close()
    except Exception as err:
        print(err);
def showWeb(rows):
        print("Showing data from Web...")
        for row in rows:
            print(row)
def showDB():
    print("Showing data from DB...")
    try:
        con = sqlite3.connect("students.db")
        cursor = con.cursor()
        #查询数据库记录
        cursor.execute("select * from students")
        rows=cursor.fetchall()
        #显示每条记录
        for row in rows:
            print(row)
        con.close()
    except Exception as err:
        print(err)
try:
    url = "http://127.0.0.1:5000"
    #访问这个网址获取 html
    resp=urllib.request.urlopen(url)
    data=resp.read()
    html=data.decode("utf-8")
    #在 html 中查找学生信息
    rows=searchWeb(html)
    #显示查找的信息
    showWeb(rows)
    #保存学生信息到数据库
    saveDB(rows)
    #显示数据库的数据
    showDB()
except Exception as e:
    print(e)