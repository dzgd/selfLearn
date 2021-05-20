import matplotlib.pyplot as plt
import matplotlib
import jieba
import jieba.analyse
from wordcloud import WordCloud
import numpy as np
from collections import Counter
# 设置字体 有的linux字体有问题
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

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
        seg_list = jieba.cut(va, cut_all=False)  ## jieba分词
        index += 1
        for x in seg_list:
            if len(x) > 1 and x != '\r\n':  # 不是单个字 并且不是特殊符号
                try:
                    c[x] += 1  # 这个单词的次数加一
                except:
                    continue
        commnetstr += va
    for (k, v) in c.most_common():  # 过滤掉次数小于5的单词
        if v < 2 or k in list:
            c.pop(k)
            continue
        # print(k,v)
    print(len(c), c)
    getciyun_most(c)  # 词云
    # print(commnetstr)
def anylase():
    comment = []
    flie = open('bilibili_danmu.txt','r',encoding= "utf-8")  # 打开bilibili_danmu.txt文件
    while True:
        data = flie.readline()
        comment.append(data)
    anylaseword(data)

if __name__ == '__main__':
    anylase()