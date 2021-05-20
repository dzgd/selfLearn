import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import tensorflow as tf
from pylab import mpl
from sklearn import datasets
mpl.rcParams['font.sans-serif'] =['SimHei']
np.random.seed(1)
tf.set_random_seed(1)
sess=tf.Session()
iris=datasets.load_iris()
x_vals=iris.data
y_vals=np.array([1 if y==0 else-1 for y in iris.target])
train_indices=np.random.choice(len(x_vals),round(len(x_vals)*0.8), replace=False)
test_indices=np.array(list(set(range(len(x_vals)))-set(train_indices)))
x_vals_train =x_vals[train_indices]
x_vals_test =x_vals[test_indices]
y_vals_train =y_vals[train_indices]
y_vals_test =y_vals[test_indices]
batch_size = 100   #设置每次训练中选取样本的容量。
#设定Tensorflow参变量。x_data为输入，y_target为真实标签，W和b为超平面的参数
x_data =tf.placeholder(shape=[None, 4], dtype=tf.float32)
y_target =tf.placeholder(shape=[None, 1], dtype=tf.float32)
W = tf.Variable(tf.random_normal(shape=[4,1]))
b =tf.Variable(tf.random_normal(shape=[1,1]))
#接下来定义可以优化的损失函数。在SVM中，我们利用Hinge Loss作为损失函数。计算结果为model_output
model_output=tf.matmul(x_data,W)+b
l2_norm =tf.reduce_sum(tf.square(W))
alpha = tf.constant([0.1])
classification_term =tf.reduce_mean(tf.maximum(0.,1.-model_output*y_target))
loss =classification_term+alpha*l2_norm
#定义模型输出。利用符号函数实现，结果大于0时，输出1，小于0时，输出-1。
prediction =tf.sign(model_output)
#定义准确率，利用的是一批样本的平均准确率。
accuracy =tf.reduce_mean(tf.cast(tf.equal(prediction, y_target),tf.float32))
#定义训练步骤。
train_step=tf.train.GradientDescentOptimizer(0.01).minimize(loss)
#开始训练，初始化所有变量。
sess.run(tf.global_variables_initializer())
#为了方便直观显示，我们定义三个数组，分别对应训练误差、训练准确率和测试准确率。
loss_vec = []
train_accuracy = []
test_accuracy = []
#在每次迭代过程当中，首先随机选择训练的样本，然后进行训练。我们设置迭代次数为200次。
for i in range(500):
    rand_index =np.random.choice(len(x_vals_train), size=batch_size)
    rand_x = x_vals_train[rand_index]
    rand_y =np.transpose([y_vals_train[rand_index]])
    sess.run(train_step, feed_dict={x_data:rand_x, y_target:rand_y})
#接下来就是直观显示结果的东西了
for i in range(200):
    temp_loss = sess.run(loss,feed_dict={x_data: rand_x, y_target: rand_y})
    loss_vec.append(temp_loss)
    train_acc_temp=sess.run(accuracy,feed_dict={x_data: x_vals_train,y_target: np.transpose([y_vals_train])})
    train_accuracy.append(train_acc_temp)
    test_acc_temp=sess.run(accuracy,feed_dict={x_data: x_vals_test,y_target: np.transpose([y_vals_test])})
    test_accuracy.append(test_acc_temp)
    if (i+1)%100==0:
        print('Step #' + str(i+1) + ' W = ' +str(sess.run(W)) + 'b = ' + str(sess.run(b)))
        print('Loss = ' + str(loss))
plt.plot(loss_vec)
plt.plot(train_accuracy)
plt.plot(test_accuracy)
plt.legend(['损失','训练精确度','测试精确度'])
plt.ylim(0.,1.)
plt.show()