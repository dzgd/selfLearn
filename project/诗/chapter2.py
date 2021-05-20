#定义，赋值
# s = 'string'      # 利用单引号声明一个字符串
# s = 1        # 默认声明一个整数
# s = 1.1      # 默认为双精度的浮点数
def example1():     # 定义函数，功能为判断输入的数字是否为2,如果为2，则打印true;如果为其他数字或者其他不是2的数据类型，打印false;
    answer = int(input("请输入一个数字："))
    if answer==2:
      print("true")
    else:
      print("false")

def example2():   # 定义函数，功能为输入一个名字，判断输入的是否为小李，若为小李，则打印”小李，你好“，否则打印”错误“
    answer = str(input("请输入你的名字："))
    if answer == "小李":
        print("小李，你好")
    else:
        print("错误")
def example3():   # 定义一个函数，功能为输入成绩，判断成绩的水平。大于90为A,80到90之间为B,其余为F
    score = float(input("请输入成绩："))
    if score>=90:
        print("A")
    elif score < 90 and score >80:
        print("B")
    else:
        print("F")
# 真 1,True
# 假 0,False
#循环1+2+3+4+5+......200
def xunhuan():
    sum=0      # 初始化和为0
    for i in range(1,201):    # 从1开始循环到200，左闭右开区间
        sum=sum+i     # 每循环一次，sum就加上i
        print(sum)     # 每次循环打印和的结果
    print("-------sum:")
    print(sum)       # 最终打印1到200的求和结果

def teststring():
    str1 = "Pythonnnnnn"     # 声明一个字符串，赋值给str1
    str2 = "Hello"   #   声明一个字符串，赋值给str2
    # print(str1)       # 打印
    #链接字符串
    # print(str1+str2)     # 字符串拼接
    # str3= str1*3        # 表示字符串连续出现3次
    # print(str3)
    # print(str1[0])# P     # 打印字符串中的第一个字符p
    # print(str1[1])  # y     # 同理
    # print(str1[-2])     # 打印倒数第二的字符
    # print(str1[2:5])     # 打印从2到4的字符，不包括第五个字符
    # print(str1.count('n'))    #打印首次出现"n"字符的位置，从1开始计算
    # print(str1.startswith('Py'))   # 如果字符串中以Py开头的，打印为true,否则为false
    # print(str1.endswith('Pn'))    #  如果字符串中以Pn结尾的，打印为true,否则为false
    if str1.endswith('Pn'):
        print("yes")
    else:
        print("No")
#列表
#定义
def leibiao():
    L = [0]     # 列表中只有一个元素
    LL = [1,2,3,4.0,5,'string']    # 列表中的元素可以是不同数据类型的
    # # print(LL)
    # L.append(LL)     #  往列表L中追加LL元素整体
    # print(L)
    for i in LL:       # 把LL元素的每一个元素提取出来
        L.append(i)     #  往列表L中追加LL元素的每一个元素
        print(L)
    print(L)

def readxingqing():
    file = open("data//星晴.txt",mode='r',encoding='utf-8')  # 打开txt文件，以只读的格式，编码为utf-8
    conent = file.readlines()     # 文件一行一行读取，直到最末尾
    for i in conent:       # 读取一行
        print(i)             #打印一行
    print("-------------------------")
    newfile = []    # 定义一个空列表用来存储文件
    for i in conent:      # 再次遍历原文件
        if i.startswith("#") or i.startswith("-"):   # 如果每一行以"#"开头或者以"-"开头的字符，就跳过
            pass
        else:
            newfile.append(i)      # 如果每一行不是以"#"开头或者以"-"开头的字符，就追加到新文件中
    for i in newfile:    # 然后遍历新文件
        print(i)       # 打印是否保存成功
#数据写入CSV文件
import csv       # 导入数据读取相关模块
def writefiles():     # 定义函数
    content = [['韩梅梅',1,2,3],['理论',3,4,5],['sala',3,4,5],['li',4,5,6]]    # 定义一个列表
    file = open('data//test.csv','w',newline="")     # 打开此csv文件，文件如果不存在，则新建；文件以写的形式给出
    content_out = csv.writer(file)     # 实例化文件类型对象
    for i in content:               # 遍历内容
        content_out.writerow(i)     # 按行写入
    file.close()                    # 关闭文件

if __name__ == '__main__':        # 运行主程序
    writefiles()            # 运行函数，得到新文件