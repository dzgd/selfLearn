a=input("请输入一个数字")
if int(a)<10:
    print("a是小于10的数字")
else:
    print("a是大于等于10的数字")


'''num=input("请输入")
print(num if(int(num)<10) else "数字太大")
'''

# if语句练习(1)
'''score=int(input("请输入分数: "))
grade=""
if score<60:
    grade="不及格"
elif score<80:
    grade="及格"
elif score<90:
    grade="良好"
else:
    grade="优秀"
print("分数是{0},等级是{1}".format(score,grade))'''
# if语句练习(2)
'''x=int(input("输入一个数字： "))
y=int(input("输入另一个数字： "))
if x==0 and x==0:
    print("原点")
elif x==0:
    print("y轴")
elif y==0:
    print("x轴")
elif x>0 and y>0:
    print("第一象限")
elif x>0 and y<0:
    print("第四象限")
elif x<0 and y>0:
    print("第二象限")
else:
    print("第三象限")'''
# while语句练习
'''num=0
while num<=10:
    print(num,end="\t")
    num+=1'''

#求和
'''num2 =0
sum =0
while num2<=100:
    sum=sum+num2
    num2+=1
print(sum)'''

#for语句练习
'''sum=0
for x in range(101):
    sum=sum+x
print(sum)'''
#for语句遍历字符串
'''for x in "syweirhfmvb":
    print(x,end="\t")'''
#for语句遍历字典
'''d={"name":"duzhigao","age":18,"job":"四川"}
for x in d:
    print(x)
for x in d.values():
    print(x)
for x in d.items():    #遍历字典的所有的“键值对”
    print(x)'''
#嵌套循环(1)
'''for x in range(5):
    for y in range(9):
        print(x,end="\t")
    print() '''  #起到换行的作用
#嵌套循环(2)九九乘法表
'''for m in range(1,10):
    for n in range(1,m+1):
        print("{0}*{1}={2}".format(m,n,(m*n)),end="\t")
    print()'''
#使用列表和字典存储表格的数据
'''r1=dict(name="高小一",age=18,salary=30000,city="北京")
r2=dict(name="高小二",age=19,salary=20000,city="上海")
r3=dict(name="高小五",age=23,salary=10000,city="深圳")
tb=[r1,r2,r3]
for x in tb:
    if x.get("salary")>15000:
        print(x)
    print()'''
#break语句练习(结束整个循环)
'''while True:    #陷入死循环
    a=input("请输入一个字符(输入Q或q时退出)： ")
    if a=="q" or a=="Q":
        print("循环结束，退出")
        break
    else:
        print(a)'''
#continue语句（结束本次循环）
#要求输入员工的薪资，若薪资小于0则重新输入。最后打印出录入员工的数量和薪资明细，以及平均薪资
'''empNum=0
salarySum=0
salarys=[]
while True:
    s=input("请输入员工的薪资（按Q或q结束）： ")
    if s.upper()=="Q":
        print("录入完成，退出")
        break
    if float(s)<0:
        continue
    empNum+=1
    salarys.append(float(s))
    salarySum+=float(s)
print("员工数:{0}".format(empNum))
print("录入薪资:",salarys)
print("平均薪资:",(salarySum/empNum))'''
 #测试zip()并行循环
'''names=("高一","高二","高三","高四","高五")
ages=(17,18,19,20,21)
jobs=("班长","学习委员","课代表","团支书")
for a,b,c in zip(names,ages,jobs):
     print("{0}--{1}--{2}".format(a,b,c))
# or
for i in range(4):
    print("{0}--{1}--{2}".format(names[i],ages[i],jobs[i]))'''
#####-----------------2020年2月17日写----------------------#####

