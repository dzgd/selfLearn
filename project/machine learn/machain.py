# from sklearn.datasets import load_iris
# #print(load_boston(return_X_y=True))
# #print(data.shape)
# # print(target)
# # print(data)
# print(load_iris())

# import tensorflow as tf
# hello = tf.constant('Hello, TensorFlow!')
# sess = tf.Session()
# print(sess.run(hello))


'''
KKT条件，
像绵延起伏的万水千山
隔断了我的视线，
却隔不断我对远方的期盼，
少年傲然，曾经，要追寻生命的最优参；

我倚核函数之剑迭代循环，
穿过水榭，越过山峦，
到达SMO算法的彼端，
人生暮然，原来，你才是我人生的最优参。       ------2020.4.9/23:28 记'''

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn import datasets
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']

np.random.seed(1)
tf.set_random_seed(1)

sess=tf.Session()
#产生数据:产生数据源，在这里我们使用sklearn自带的iris数据集。
# 该数据集为鸢尾花数据集，一共有150个数据：这些数据分为3类（山鸢尾、杂色鸢尾和维吉尼亚鸢尾），每类50个数据。
# 这些数据主要包括四个属性：萼片长度、萼片宽度、花瓣长度、花瓣宽度。在这里我们主要实现二分类，
# 所以将山鸢尾标签置为1，其他两种为-1。
iris=datasets.load_iris()
x_vals=iris.data
y_vals=np.array([1 if y==0 else -1 for y in iris.target])
#划分数据为训练集和测试集
#接下来，将数据集划分为训练集和测试集，这里我们使用np.random.choice()方法来随机划分。
# 其中，x_vals_train、y_vals_train为训练集的样本和标签，x_vals_test和y_vals_test为测试集的样本和标签。
# 测试集和训练集的比例我们设置为8:2。
train_indices = np.random.choice(len(x_vals),round(len(x_vals)*0.8), replace=False)
test_indices = np.array(list(set(range(len(x_vals))) - set(train_indices)))
x_vals_train = x_vals[train_indices]
x_vals_test = x_vals[test_indices]
y_vals_train = y_vals[train_indices]
y_vals_test = y_vals[test_indices]
#批训练中批的大小
#设定Tensorflow参变量。x_data为输入，y_target为真实标签，W和b为超平面的参数。
batch_size = 100
x_data = tf.placeholder(shape=[None, 4], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)
W = tf.Variable(tf.random_normal(shape=[4,1]))
b = tf.Variable(tf.random_normal(shape=[1,1]))
#定义损失函数
model_output=tf.matmul(x_data,W)+b
l2_norm = tf.reduce_sum(tf.square(W))
#软正则化参数
alpha = tf.constant([0.1])
#定义损失函数
#在SVM中，我们利用Hinge Loss作为损失函数。计算结果为model_output，
classification_term = tf.reduce_mean(tf.maximum(0.,1.-model_output*y_target))
loss = classification_term+alpha*l2_norm
#输出:定义模型输出。利用符号函数实现，结果大于0时，输出1，小于0时，输出-1。
prediction = tf.sign(model_output)
accuracy = tf.reduce_mean(tf.cast(tf.equal(prediction, y_target),tf.float32))
train_step=tf.train.GradientDescentOptimizer(0.01).minimize(loss)
#开始训练:初始化所有变量。
sess.run(tf.global_variables_initializer())
loss_vec = []
train_accuracy = []
test_accuracy = []
for i in range(200):
    rand_index = np.random.choice(len(x_vals_train), size=batch_size)
    rand_x = x_vals_train[rand_index]
    rand_y = np.transpose([y_vals_train[rand_index]])
    sess.run(train_step, feed_dict={x_data: rand_x, y_target:rand_y})
    temp_loss = sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})
    loss_vec.append(temp_loss)
    train_acc_temp = sess.run(accuracy, feed_dict={x_data: x_vals_train, y_target: np.transpose([y_vals_train])})
    train_accuracy.append(train_acc_temp)
    test_acc_temp = sess.run(accuracy, feed_dict={x_data: x_vals_test, y_target: np.transpose([y_vals_test])})
    test_accuracy.append(test_acc_temp)
    if (i+1)%100==0:
        print('Step #' + str(i+1) + ' W = ' + str(sess.run(W)) + 'b = ' + str(sess.run(b)))
        print('Loss = ' + str(test_acc_temp))
plt.plot(loss_vec)
plt.plot(train_accuracy)
plt.plot(test_accuracy)
plt.legend(['损失','训练精确度','测试精确度'])
plt.ylim(0.,1.)
plt.show()

