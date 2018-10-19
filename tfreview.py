import tensorflow as tf
import pandas,numpy as pa,np
'''w1=tf.Variable(tf.random_normal((2,3),stddev=1,seed=1))
w2=tf.Variable(tf.random_normal((3,1),stddev=1,seed=1))

x=tf.constant([[0.7,0.9]])
x=tf.placeholder()
a=tf.matmul(x,w1)
y=tf.matmul(a,w2)

with tf.Session() as s:
    init=tf.global_variables_initializer()
    s.run(init)
    print(s.run(y))
'''
from numpy.random import RandomState

#定义训练集大小
batch_size=8
#定义权重
w1=tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2=tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))
x=tf.placeholder(tf.float32,shape=(None,2),name='x_input')
y_=tf.placeholder(tf.float32,shape=(None,1),name='y_input')

#定义NN前向传播过程
a=tf.matmul(x,w1)
y=tf.matmul(a,w2)

#定义损失函数和反向传播算法
y=tf.sigmoid(y)
cross_entropy=-tf.reduce_mean(y_*tf.log(tf.clip_by_value(y,1e-10,1.0))+(1-y)*tf.log(tf.clip_by_value(1-y,1e-10,1.0)))
train_step=tf.train.AdamOptimizer(0.1).minimize(cross_entropy)

#通过随机数生成训练集
rdm=RandomState(1)
dataset_size=128
X=rdm.rand(dataset_size,2)
Y=[[int ((x1+x2)<1)] for(x1,x2) in X]
#创建会话运行
with tf.Session() as s:
    init=tf.global_variables_initializer()
    s.run(init)
    print(s.run(w1))
    #设置训练轮数
    step=20
    # 每次选取batch_size个样本进行训练
    for i in range(step):
        start=(i*batch_size)%dataset_size
        end=min(start+batch_size,dataset_size)
        s.run(train_step,feed_dict={x:X[start:end],y_:Y[start:end]})
    print(s.run(w1))
    print(w1[1][1])





