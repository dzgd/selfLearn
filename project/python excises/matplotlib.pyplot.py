import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
# 准备数据
movie_name = ['雷神3：诸神黄昏','正义联盟','东方快车谋杀案','寻梦环游记','全球风暴','降魔传','追捕','七十七天','密战','狂兽','其它']
place_count = [60605,54546,45819,28243,13270,9945,7679,6799,6101,4621,20105]
# 展示
plt.pie(place_count, labels=movie_name,autopct="%1.2f%%")
# 显示图例
plt.legend()
# 添加标题
plt.title("电影排片占比")
# 规定为正圆
plt.axis('equal')
plt.show()

'''
import numpy as np
import matplotlib.pyplot as plt
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
# 指定颜色和大小，数据
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.show()
'''


'''
import matplotlib.pyplot as plt
arr1 = [131,  98, 125, 131, 124, 139, 131, 117, 128, 108, 135, 138, 131, 102, 107, 114, 119, 128,\
       121, 142, 127, 130, 124, 101, 110, 116, 117, 110, 128, 128, 115,  99, 136, 126, 134,]
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['font.size'] = 20  # 修改字体大小
plt.rcParams['axes.unicode_minus'] = False  # 字体是中文时显示负数会有bug，去除一下
# 展示刻度
plt.xticks(range(min(arr1), max(arr1))[::4])
# 个数
bins = (max(arr1) - min(arr1)) // 4
print(bins)
plt.hist(arr1, bins=bins, density=1, alpha=0.8)
plt.grid(True, linestyle="--", alpha=0.5)
plt.ylabel('数量')
plt.title('直方图')
plt.show()'''


'''
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 中文
x = np.arange(5)
y1 = np.random.randint(10,100,5)
y2 = np.random.randint(10,100,5)
fig = plt.figure()
# fig.add_subplot(1,2,1)
# 指定x，y的值
plt.bar(x, y1,width=0.4,label='第一组')
# fig.add_subplot(1,2,2)
plt.bar(x+0.4,y2,width=0.4,label='第二组')
# 显示图例
plt.legend()
plt.show()
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#散点图
# N=100
# x=np.random.randn(N)
# y=np.random.randn(N)
# plt.scatter(x,y,marker="+")
# # plt.show()
# df=pd.DataFrame({"x":x,"y":y})
# sns.relplot(x="x",y="y",data=df,kind="scatter",marker="x")
# plt.show()
#折线图
# x=[2007,2008,2009,2010,2011,2012,2013]
# y=[2,4,11,54,65,23,10]
# plt.plot(x,y)
# plt.show()
# df=pd.DataFrame({"x":x,"y":y})
# sns.lineplot(x="x",y="y",data=df)
# plt.show()
#直方图
#a=np.random.randn(100)
# s=pd.Series(a)
# plt.hist(s)
# plt.show()
# sns.distplot(s,kde=False)
# plt.show()
# sns.distplot(s,kde=True)
# plt.show()
#t条形图
# x=["col1","col2","col3","col4","col5"]
# y=[6,4,7,11,9]
# plt.bar(x,y)
# plt.show()
# sns.barplot(x,y)  #自动设置颜色
# plt.show()
#箱线图
# data=np.random.normal(size=(10,4))
# labels=["A","B","C","D"]
# plt.boxplot(data,labels=labels)
# plt.show()
# df=pd.DataFrame(data,columns=labels)
# sns.boxplot(data=df)  #自动上色
# plt.show()
#饼图
# nums = [20, 36, 40, 37, 6]
# labels = ['High-school','Bachelor','Master','Ph.d', 'Others']
# # 用 Matplotlib 绘制饼图
# plt.pie(x = nums, labels=labels)
# plt.show()
# #热力图
# flights=sns.load_dataset("flights")
# flights=flights.pivot("month","year","passengers")  #生成热力图之前先制作透视表pivot
# ax=sns.heatmap(flights,annot=True,fmt="d")
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.font_manager import FontProperties
#雷达图
'''
#数据准备
labels=np.array([u"推进","KDA",u"生存",u"团战",u"发育",u"输出"])
states=[20,50,9,47,56,88]
#绘图数据准备，角度，状态值
angles=np.linspace(0,2*np.pi,len(labels),endpoint=False)
states=np.concatenate((states,[states[0]]))#numpy提供了numpy.concatenate((a1,a2,...), axis=0)函数。
# 能够一次完成多个数组的拼接。其中a1,a2,...是数组类型的参数
angles=np.concatenate((angles,[angles[0]]))
fig=plt.figure()
ax=fig.add_subplot(111,polar=True)
ax.plot(angles,states,"o-",linewidth=2)
ax.fill(angles,states,alpha=0.25)
#设置中文字体
font=FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
ax.set_thetagrids(angles * 180/np.pi, labels, FontProperties=font)
plt.show()
'''
#******画两个变量的相关图
# tips=pd.read_csv(r"F:\面板数据文件\seaborn\seaborn-data-master\seaborn-data-master\tips.csv")
# sns.jointplot(x="total_bill",y="tip",data=tips,kind="scatter")
# sns.jointplot(x="total_bill",y="tip",data=tips,kind="kde")
# sns.jointplot(x="total_bill",y="tip",data=tips,kind="hex")
#plt.show()



#*****画鸢尾花的多个变量的分布相关图
# iris=pd.read_csv("F:\\面板数据文件\\seaborn\\seaborn-data-master\\seaborn-data-master\\iris.csv")
# #使用seaborn绘制成对关系
# sns.pairplot(iris)
# plt.show()

'''
#对np.append()和np.concatenate()两个函数的运行时间进行比较
from time import clock as now
a=np.arange(9999)
b=np.arange(9999)
time1=now()
c=np.append(a,b)
time2=now()
print(time2-time1)
w=np.arange(9999)
n=np.arange(9999)
ptime1=now()
q=np.concatenate((a,b),axis=0)
ptime2=now()
print(ptime2-ptime1)
'''

'''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
titanic=pd.read_csv("F:\\面板数据文件\\seaborn\\seaborn-data-master\\seaborn-data-master\\titanic.csv")
#sns.barplot(x="class",y="survived",data=titanic)
# print(titanic.head())
# print(titanic.tail())
#年龄直方图，先删除缺失值
age1=titanic["age"].dropna()
sns.distplot(age1)''' #distplot() 默认拟合出了密度曲线,'kde' 是控制密度估计曲线的参数，默认为 True，不设置会默认显示，如果我们将其设为 False，则不显示密度曲线。
#sns.distplot(age1,bins=30,kde=False)
#plt.show()

#'rug' 参数用于控制直方图中的边际毛毯，通过控制'rug'是实现毛毯是否显示。
#创建一个一行2列的画布,主要方便对比
#fig,axes=plt.subplots(1,2)

#设置'rug'参数，加上观测数值的边际毛毯
#需要用axes[]表示是第几张图，从0开始
# sns.distplot(age1,ax=axes[0]) #左图
# sns.distplot(age1,rug=True,ax=axes[1]) #右图
# plt.show()


#当然，除了控制矩形分布、密度曲线及边际毛毯是否显示，还可以通过更丰富的参数控制他们展示的细节，
#这些通过参数 'hist_kws' 、'kde_kws' 、'reg_kws' 来进行设置，因为其中涉及到多个参数，参数间用逗号隔开，
# 参数外面用大括号括住。
'''
fig,axes=plt.subplots(1,2)
sns.distplot(age1,rug=True,ax=axes[0])
sns.distplot(age1,rug=True,hist_kws={"color":"green","label":"hist"},\
             kde_kws={"color":"red","label":"KDE"},\
             ax=axes[1])
plt.show()
'''

#条形图
#barplot() 利用矩阵条的高度反映数值变量的集中趋势，以及使用errorbar功能（差棒图）来估计变量之间的差值统计（置信区间）。
# 需要提醒的是 barplot() 默认展示的是某种变量分布的平均值（可通过参数修改为 max、median 等）。
# sns.barplot(x="class",y="survived",data=titanic)
# # plt.show()

#********
#我们可以通过设置'hue'参数，对x轴的数据进行细分，细分的条件就是'hue'的参数值，
#比如这里我们的x轴是'class'（仓位等级），我们将其按'sex'（性别）再进行细分。
# sns.barplot(x="class",y="survived",hue="sex",data=titanic)
# plt.show()
# sns.barplot(x="embarked",y="survived",hue="class",data=titanic)
# plt.show()

#**计数图countplot
# sns.countplot(x="deck",data=titanic)
# plt.show()


# fig,axes=plt.subplots(1,2)
# sns.countplot(x="deck",hue="sex",data=titanic,ax=axes[0])
# sns.countplot(y="deck",hue="sex",data=titanic,ax=axes[1])
# plt.show()

#********散点图
#在seaborn中有两种不同的分类散点图。
# stripplot() 使用的方法是用少量的随机“抖动”调整分类轴上的点的位置，
# swarmplot() 表示的是带分布属性的散点图。
#同时可以通过设置'jitter'参数控制抖动的大小。

'''
fig,axes=plt.subplots(2,2)
sns.stripplot(x="embarked",y="fare",data=titanic,ax=axes[0][0],jitter=1)
#swarmplot() 方法使用防止它们重叠的算法沿着分类轴调整点。
# 它可以更好地表示观测的分布，它适用于相对较小的数据集。
sns.swarmplot(x="embarked",y="fare",data=titanic,ax=axes[0][1])
sns.stripplot(x="embarked",y="age",hue="who",jitter=1,data=titanic,ax=axes[1][0])
sns.swarmplot(x='embarked',y='age',hue='who',data=titanic,ax=axes[1][1])
plt.show()
'''
# fig,axes=plt.subplots(1,2)
# sns.boxplot(x='class',y='age',hue='who',data=titanic,ax=axes[0])
# sns.boxplot(x='age',y='class',hue='who',data=titanic,ax=axes[1])
# plt.show()


