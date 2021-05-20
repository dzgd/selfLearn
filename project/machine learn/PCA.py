'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

#  #归一化
# def featureNormalize(X):
#     （每一个数据-当前列的均值）/当前列的标准差
#     n = X.shape[1]
#     mu = np.zeros((1,n))
#     sigma = np.zeros(1,n)
#     mu = np.mean(X,axis=0)
#     sigma = np.std(X,axis=0)
#     for i in range(n):
#         X[:,i] = (X[:,i]-mu[i])/sigma[i]
#     return X,mu,sigma

# iris=load_iris()
# X=iris.data
# X_norm=StandardScaler().fit_transform(X)
# ew,ev=np.linalg.eig(np.cov(X_norm.T))# np.cov直接求协方差矩阵，每一行代表一个特征，每一轮代表样本
# ew_order=np.argsort(ew)[::-1]###特征值从大到小排序
# ew_sort=ew[ew_order]
# ev_sort=ev[:,ew_order]
# K=2
# V=ev_sort[:,:2]
# X_new=X_norm.dot(V)
# colors=["red","black","orange"]
# plt.figure()
# for i in [0,1,2]:
#     plt.scatter(X_new[iris.target==i,0],X_new[iris.target==i,1]\
#                 ,alpha=.7,c=colors[i],label=iris.target_names[i])
# plt.legend()
# plt.title("PCA of IRIS dataset")
# plt.xlabel("PC_0")
# plt.ylabel("PC_1")
# plt.show()


from sklearn.decomposition import PCA
pca=PCA(n_components=2)
X_new=pca.fit_transform(X_norm)#用X来训练PCA模型，同时返回降维后的数据。
"""查看PCA的一些属性"""
print(pca.explained_variance_)    # 属性可以查看降维后的每个特征向量上所带的信息量大小（可解释性方差的大小）
print(pca.explained_variance_ratio_)  # 查看降维后的每个新特征的信息量占原始数据总信息量的百分比
print(pca.explained_variance_ratio_.sum())    # 降维后信息保留量
##怎么选择n_coments呢？《画图，选转择点》
pca_line=PCA().fit(X_norm)
plt.plot([1,2,3,4],np.cumsum(pca_line.explained_variance_ratio_))
plt.xticks([1,2,3,4])
plt.xlabel("number of components after dimension reduction")
plt.ylabel("cumulative explained variance ratio")
plt.show()
'''

from graphviz import Digraph
dot = Digraph(comment='The Round Table')
# 添加圆点 A, A的标签是 King Arthur
dot.node('A', 'king')
dot.view()  #后面这句就注释了，也可以使用这个命令查看效果 # 添加圆点 B, B的标签是 Sir Bedevere the Wise
dot.node('B', 'Sir Bedevere the Wise')

dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])

dot.edge('B', 'L', constraint='false')

print(dot.source) # 保存source到文件，并提供Graphviz引擎

