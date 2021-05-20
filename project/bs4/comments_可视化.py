import matplotlib.pyplot as plt
import matplotlib
import jieba
import jieba.analyse
import xlwt
import xlrd
from wordcloud import WordCloud
import numpy as np
from collections import Counter
# 设置字体 有的linux字体有问题
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


# 类似comment 为评论的一些数据 [  ['1','名称'，'star星','赞同数','评论内容']  ,['2','名称'，'star星','赞同数','评论内容'] ]元组
def anylasescore(comment):
    score = [0, 0, 0, 0, 0, 0]  # 分别对应0 1 2 3 4 5分出现的次数
    count = 0  # 评分总次数
    for va in comment:  # 遍历每条评论的数据  ['1','名称'，'star星','赞同数','评论内容']
        try:
            score[int(va[2])] += 1  # 第3列 为star星 要强制转换成int格式
            count += 1
        except Exception as e:
            continue
    print(score)
    label = '1分', '2分', '3分', '4分', '5分'
    color = 'blue', 'orange', 'yellow', 'green', 'red'  # 各类别颜色
    size = [0, 0, 0, 0, 0]  # 一个百分比数字 合起来为100
    explode = [0, 0, 0, 0, 0]  # explode :(每一块)离开中心距离；
    for i in range(5):  # 计算
        size[i] = score[i+1] * 100 / count
        explode[i] = score[i+1] / count / 10
    pie = plt.pie(size, colors=color, explode=explode, labels=label, shadow=True, autopct='%1.1f%%')
    for font in pie[1]:
        font.set_size(8)
    for digit in pie[2]:
        digit.set_size(8)
    plt.axis('equal')  # 该行代码使饼图长宽相等
    plt.title(u'各个评分占比', fontsize=12)  # 标题
    plt.legend(loc=0, bbox_to_anchor=(0.82, 1))  # 图例
    # 设置legend的字体大小
    leg = plt.gca().get_legend()
    ltext = leg.get_texts()
    plt.setp(ltext, fontsize=6)
    plt.savefig("score.png")
    # 显示图
    plt.show()


def getzhifang(map):  # 直方图二维，需要x和y两个坐标
    x = []
    y = []
    for k, v in map.most_common(15):  # 获取前15个最大数值
        x.append(k)
        y.append(v)
    Xi = np.array(x)  # 转成numpy的坐标
    Yi = np.array(y)

    width = 0.6
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.figure(figsize=(8, 6))  # 指定图像比例：8：6
    plt.bar(Xi, Yi, width, color='blue', label='热门词频统计', alpha=0.8, )

    plt.xlabel("词频")
    plt.ylabel("次数")
    plt.savefig('zhifang.png')
    plt.show()
    return


def getciyun_most(map):  # 获取词云
    # 一个存对应中文单词，一个存对应次数
    x = []
    y = []
    for k, v in map.most_common(300):  # 在前300个常用词语中
        x.append(k)
        y.append(v)
    xi = x[0:150]  # 截取前150个
    xi = ' '.join(xi)  # 以空格 ` `将其分割为固定格式(词云需要)
    print(xi)
    backgroud_Image = plt.imread(r'C:\Users\Administrator\Desktop\统计师\报名照片.jpg')  # 如果需要个性化词云
    # 词云大小，字体等基本设置
    wc = WordCloud(background_color="white",
                   width=1500, height=1200,
                   # min_font_size=40,
                   mask=backgroud_Image,
                   font_path="simhei.ttf",
                   max_font_size=150,  # 设置字体最大值
                   random_state=50,  # 设置有多少种随机生成状态，即有多少种配色方案
                   )  # 字体这里有个坑，一定要设这个参数。否则会显示一堆小方框wc.font_path="simhei.ttf"   # 黑体
    # wc.font_path="simhei.ttf"
    my_wordcloud = wc.generate(xi)  #需要放入词云的单词 ，这里前150个单词
    plt.imshow(my_wordcloud)  # 展示
    my_wordcloud.to_file("img.jpg")  # 保存
    xi = ' '.join(x[150:300])  # 再次获取后150个单词再保存一张词云
    my_wordcloud = wc.generate(xi)
    my_wordcloud.to_file("img2.jpg")

    plt.axis("off")


def anylaseword(comment):
    # 这个过滤词，有些词语没意义需要过滤掉
    list = ['这个', '一个', '不少', '起来', '没有', '就是', '不是', '那个', '还是', '剧情', '这样', '那样', '这种', '那种', '故事', '人物', '什么']
    #print(list)
    commnetstr = ''  # 评论的字符串
    c = Counter()  # python一种数据集合，用来存储字典
    index = 0
    for va in comment:
        seg_list = jieba.cut(va[4], cut_all=False)  ## jieba分词
        index += 1
        for x in seg_list:
            if len(x) > 1 and x != '\r\n':  # 不是单个字 并且不是特殊符号
                try:
                    c[x] += 1  # 这个单词的次数加一
                except:
                    continue
        commnetstr += va[4]
    for (k, v) in c.most_common():  # 过滤掉次数小于5的单词
        if v < 5 or k in list:
            c.pop(k)
            continue
        # print(k,v)
    print(len(c), c)
    getzhifang(c)  # 用这个数据进行画直方图
    getciyun_most(c)  # 词云
    # print(commnetstr)


def anylase():
    data = xlrd.open_workbook('test.xls')  # 打开xls文件
    table = data.sheets()[0]  # 打开第i张表
    nrows = table.nrows  # 若干列的一个集合，是个数量单位
    comment = []
    print(nrows)  #501

    for i in range(nrows):
        comment.append(table.row_values(i))  # 将该列数据添加到元组中，为[ [  ] ,[ ] , [ ] ...]格式
    #print(comment)
    anylasescore(comment)
    anylaseword(comment)


if __name__ == '__main__':
    anylase()