import tensorflow as tf
from numpy.random import RandomState

batch_size=8
#两个输入节点
x=tf.placeholder(tf.float32,shape=(None,2),name='x_input')
y_=tf.placeholder(tf.float32,shape=(None,1),name="y_input")

#定义神经网络向前传播算法
w1=tf.Variable(tf.random_normal([2,1],stddev=1,seed=1))
y=tf.matmul(x,w1)

#定义预测多了和预测少了的成本
loss_less=10
loss_more=1

loss=tf.reduce_sum(tf.where(tf.greater(y,y_),(y-y_)*loss_more,(y_-y)*loss_less))
train_step=tf.train.AdamOptimizer(0.001).minimize(loss)

#通过随机数生成一个模拟数据集
rdm=RandomState(1)
data_size=128
#产生一个128行2列的矩阵
X=rdm.rand(data_size,2)
Y=[[x1+x2+rdm.rand()/10.0-0.05]for (x1,x2) in X]

#训练神经网络
with tf.Session() as sess:
    init_op=tf.global_variables_initializer()
    sess.run(init_op)
    STEPS=5000
    for i in range(STEPS):
        start=(i*batch_size)%data_size
        end=min(start+batch_size,data_size)
        sess.run(train_step,feed_dict={x:X[start:end],y_:Y[start:end]})
        print(sess.run(w1))
