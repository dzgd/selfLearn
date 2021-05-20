#列表推导式
'''y=[x*2 for x in range(1,5)]
print(y)
a=[a for a in "abcdefghijklmn"]
print(a)
#等价于
y=[]
for x in range(1,5):
    y.append(x*2)
print(y)
#坐标输出
cells = [(row,col) for row in range(1,10) for col in range(1,10)]
print(cells)'''

#字典推导式（统计文本中字符出现的次数）
'''my_text = "i love you,i love sxt, i love duzhigao"
char_count={k:my_text.count(k) for k in my_text}
print(char_count)'''
#集合推导式
'''y={x for x in range(1,100) if x%9==0}
print(y)'''
#元组生成器只能遍历一次
'''y=(x for x in range(8))
print(tuple(y))
print(tuple(y))'''

#同心圆练习
'''import turtle
t=turtle.Pen()
my_color=("red","yellow","blue","green","black")
t.width(4)
t.speed(0)
for i in range(20):
    t.penup()
    t.goto(0,-i*10)
    t.pendown()
    t.color(my_color[i%len(my_color)])
    t.circle(10+i*10)
turtle.done()  #显示画布'''

#函数的定义和调用
'''def fun01():
    print("*"*10)
    print("$"*10)
fun01()
fun01()'''
#比较大小
'''def fun02(a,b):

    if a>b:
        print(a,"较大值")
    else:
        print(b,"较大值")
fun02(45,78)
help(fun02.__doc__)   #用于打印解释字符串'''

#测试Reture的用法
'''def  add(a,b):
    print("计算两个数的和： {0},{1},{2}".format(a,b,(a+b)))
    return a+b
add(40,60)
print(add(40,60)*8)   #多输入一个返回值'''
#参数的传递(可变对象)
'''a=[10,20]
print(id(a))
print(a)
def fun03(m):
    print(id(m))
    m.append(30)
    print(id(m))
    print(m)
    print(id(m))
fun03(a)'''
#参数的传递（不可变对象)
'''a=100
def fun04(n):
    print("n",id(n))  #有引号打印出来的是字符
    n=n+200
    print("n",id(n))
    print(n)          #没引号打印出来的是数字
fun04(a)
print("a",id(a))'''
#浅拷贝，深拷贝
'''import copy
a=[10,20,[5,6]]
b=copy.copy(a)
print("a",a)
print("b",b)
b.append(30)   #b自己增加的对象
b[2].append(7)  #b通过索引a增加的对象导致a的值发生变化
print("浅拷贝.....")
print("a",a)
print("b",b)'''
'''import  copy
a=[10,20,[5,6]]
b=copy.deepcopy(a)
print("a",a)
print("b",b)
b.append(30)   #b自己增加的对象
b[2].append(7)  #b通过深拷贝把a的所有对象都拷贝了，现在就通过自己增加对象
print("深拷贝.....")
print("a",a)
print("b",b)'''
#传递不可变对象（元组）：不可变对象包含了子对象是可变的，则方法内修改了这个可变对象，源对象也发生了变化
'''a=(10,20,[5,6])
print("a",id(a))
def fun05(m):
    print("m",id(m))
    m[2][0]=888   #元组不能改变对象，但是元组下面的列表可以改变
    print(m)
    print("m",id(m))
fun05(a)
print(a)'''
#lambda表达式可以用来声明匿名函数。lambda函数是一种简单的、在同一行中定义函数的方法。lambda函数实际生成了一个函数对象
'''f=lambda a,b,c:a+b+c
print(f)
print(f(2,3,4))
g=[lambda a:a*2,lambda b:b*3,lambda c:c*4]
print(g[0](6),g[1](7),g[2](8))'''
#eval()函数:将字符串当成有效的表达式来求值并返回计算结果
'''a=55
b=23
c=eval("a+b")     #必须是字符串对象
print(c)
dict1=dict(a=100,b=200)
d=eval("a+b",dict1)
print(d)'''
#递归函数的基本原理
'''def fun06(m):
    print("fun06",m)
    if m==0:
        print("over")
    else:
        fun06(m-1)
    print("fun06****",m)
fun06(6)'''
#阶乘的计算
'''def fun07(m):
    if m==1:
        return 1
    else:
        return m*fun07(m-1)
print(fun07(5))'''
#嵌套函数
'''def fun08():
    print("fun08 running")
    def fun09():
        print("fun09 running")
    fun09()
fun08()'''
# 测试nonlocal、global关键字的用法
'''a=1000     #全局变量
def outer():
    b=10
    def inner():
        nonlocal b    #声明外部函数的局部变量
        print("inner b: ",b)
        b=20
        global  a
        a=500
    inner()
    print("outer b: ",b)
outer()
print("a",a)'''
#类的定义
'''class Student:    #类首字母大写，多个单词采用驼峰原则
    def __init__(self,name,score):     #self必须位于第一个参数
        self.name=name
        self.score=score
    def say_score(self):         #self必须位于第一个参数
        print("{0}的分数是： {1}".format(self.name,self.score))
s1=Student("杜志高",97)
s1.say_score()
print(s1)
Student.say_score(s1)
#类也是对象
s=Student
s0=s("杜金",99)
s0.say_score()'''
#类属性的使用测试
'''class Stduent:
    school="西安财经大学"     #类属性
    count=0                  #类属性
    def __init__(self,name,score):
        self.name=name
        self.score=score
        Stduent.count=Stduent.count+1
    def say_score(self):
        print("我的学校是：",Stduent.school)
        print(self.name,"的分数是：",self.score)
s1=Stduent("杜志高",80)
s1.say_score()
s2=Stduent("杜金",99)
s2.say_score()
print("一共创建{0}个Student对象".format(Stduent.count))'''
#类方法




#析构方法__del__:用于实现对象被销毁时所需的操作。比如：释放对象占用的资源，例如：打开的文件资源
'''class Person:
    def __del__(self):
        print("销毁对象:{0}".format(self))
p1=Person()
p2=Person()
print(id(p1))
print(id(p2))
del p2
print("程序结束")'''
#__call__方法和可调用对象：即该对象可以像函数一样被调用
'''class SalaryAccount:
    def __call__(self, salary):
        print("算工资啦....")
        yearsalary=salary*12
        daysalary=salary//22.5
        hoursalary=daysalary//8
        return dict(yearsalary=yearsalary,monthsalary=salary,daysalary=daysalary,hoursalary=hoursalary)
s=SalaryAccount()
s1=s(30000)
print(s1)'''
# 测试方法的动态性
'''class Person:
    def work(self):
        print("努力上班：")
def play_game(a):
        print("{0}在玩游戏".format(a))
def work2(a):
        print("好好上班，努力工作！！！赚大钱，娶媳妇")
Person.play = play_game      #对象传递
p = Person()
p.work()
p.play()
Person.work = work2              #对象传递，改变类的函数
p.work()'''
#私有属性
'''class Exployee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
e=Exployee("杜志高",23)
print(e.name)
print(e.age)'''
#如果不想让人知道年龄，可以加双下划线访问不了;如果要访问,格式为:单下划线加类名加双下划线
'''class Employee:
    __company="百战程序员"              #私有类属性
    def __init__(self,name,age):
        self.name=name
        self.__age=age    #私有属性，加双下划线
    def __work(self):     #私有方法，加双下划线
        print("好好编程，发论文！!!")
        print("年龄：{0}".format(self.__age))     #类中方法调用其他方法中的属性
        print(Employee.__company)
e=Employee("杜志高",23)
print(e.name)
print(e._Employee__age)                #私有属性调用
print(e._Employee__work())             #私有方法调用
print(Employee._Employee__company)     #调用类属性的访问'''
#@property装饰器
#第一种情况
'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
e=Employee("杜志高",30000)
print(e.salary)
e.salary=-20000      #可改变实例属性的值
print(e.salary)'''
#第二种情况
'''class Employee:
    def __init__(self,name,salary):
        self.__name=name                   #先私有属性
        self.__salary=salary               #私有属性
        
    def get_salary(self):                  #get方法
        return self.__salary
    def set_salary(self,salary):           #set方法中传一个参数进去
        if 1000<salary<50000:
            self.__salary= salary
        else:
            print("录入错误！薪水在1000--50000这个范围")
e=Employee("杜志高",30000)
print(e.get_salary())
e.set_salary(-20000)
print(e.get_salary())'''
#第三种情况：修饰器
'''class Employee:
    def __init__(self,name,salary):
        self.__name=name               #设置私有属性
        self.__salary=salary           #设置私有属性
    @property                          #装饰的目的是使输出格式不在繁琐，体现在295行；
    def salary(self): 
        return self.__salary
e=Employee("杜志高",30000)
print(e.salary)'''
#第四种情况
'''class Employee:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
    @property                    #相当于get方法
    def salary(self):
        return self.__salary
    @salary.setter              #相当于set方法
    def salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print("录入错误！薪水在1000--50000这个范围")
e=Employee("杜志高",30000)
print(e.salary)
e.salary=-2000
print(e.salary)'''
#面向对象的三大特征：封装、继承、多态
              #（1）继承
'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_age(self):
        print("年龄，我也不知道")
class Student(Person):                 #子类继承父类方法
    def __init__(self, name, age,score):
       Person.__init__(self,name,age)
       self.score=score
print(Student.mro())
s=Student("高其",18,90)
print(s.name)
print(s.score)
print(dir(s))                #查看类的属性'''
#私有属性
'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def say_age(self):
        print("年龄，我也不知道")
class Student(Person):                 #子类继承父类方法
    def __init__(self, name, age,score):
       Person.__init__(self,name,age)
       self.score=score
print(Student.mro())                   #可以输出这个类的继承层次结构
s=Student("高其",18,90)
print(s._Person__age)                #访问私有属性'''
#方法的重写：子类可以重新定义父类中的方法，这样就会覆盖父类的方法。
#object()类是所有类的父类
#__str__():表示重写
'''class Person:
    def __init__(self,name):
        self.name=name
    def __str__(self):                #定义这个方法后输出结果就变了
        return "名字是：{0}".format(self.name)
p=Person("高企")
print(p)'''
#多态：是指同一种方法调用由于对象不同可能会产生不同的行为
'''class Man:
    def eat(self):
        print("饿了，吃饭啦！")
class Chinese(Man):
    def eat(self):
        print("中国人用筷子吃饭")
class English(Man):
    def eat(self):
        print("英国人用叉子吃饭")
class India(Man):
    def eat(self):
        print("印度人用右手吃饭")
def manEat(m):
    if isinstance(m,Man):
        m.eat()
    else:
        print("不能吃饭")
t=Man()
print(t.eat())
manEat(Chinese())
manEat(English())'''
#不小于用户输入数的最小质数
'''import math
def fun01(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    else:
        return True
n=int(input("please input an integer"))
t=n
while not fun01(t):
    t=t+1
print("Next prime number is:{0}".format(t))
print("Next prime number is:%2.2d" % (t))'''



import requests
from bs4 import BeautifulSoup
import bs4
def getHTWLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "爬取失败"
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tag in soup.find("tbody").children:
        if isinstance(tag,bs4.element.Tag):
            tds=tag("td")
            ulist.append([tds[0].string,tds[1].string,tds[3].string])

def printUnivList(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))
    for i in range(num):
        u =ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
def main():
    uinfo=[]
    url="http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html"
    html=getHTWLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)



'''b = a[i:j]   表示复制a[i]到a[j-1]，以生成新的list对象

a = [0,1,2,3,4,5,6,7,8,9]
b = a[1:3]   # [1,2]
当i缺省时，默认为0，即 a[:3]相当于 a[0:3]
当j缺省时，默认为len(alist), 即a[1:]相当于a[1:10]
当i,j都缺省时，a[:]就相当于完整复制一份a

b = a[i:j:s]表示：i,j与上面的一样，但s表示步进，缺省为1.
所以a[i:j:1]相当于a[i:j]
当s<0时，i缺省时，默认为-1. j缺省时，默认为-len(a)-1
所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍，即倒序。


###########################################################################################################
import numpy as np
a=np.random.rand(5)
print(a)
[ 0.64061262 0.8451399  0.965673  0.89256687 0.48518743]
  
print(a[-1]) ###取最后一个元素
[0.48518743]
  
print(a[:-1]) ### 除了最后一个取全部
[ 0.64061262 0.8451399  0.965673  0.89256687]
  
print(a[::-1]) ### 取从后向前（相反）的元素
[ 0.48518743 0.89256687 0.965673  0.8451399  0.64061262]
  
print(a[2::-1]) ### 取从下标为2的元素翻转读取
[ 0.965673 0.8451399  0.64061262]

'''



'''decode的作用是将二进制数据解码成unicode编码，如str1.decode('utf-8'),表示将utf-8的编码字符串解码成unicode编码。
 简单的来说：decode就是把二进制数据(bytes)转化成人看的懂得英文或者汉字(decode用的比较多)
encode的作用是将unicode编码的字符串编码成二进制数据，如str2.encode('utf-8'),表示将unicode编码的字符串编码成utf-8。'''