import tensorflow as tf
from numpy.random import RandomState
#定义训练集大小
batch_size=8

#定义神经网络参数
w1=tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2=tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))
x_data=tf.placeholder(tf.float32,shape=(None,2),name='x_data')
y_data=tf.placeholder(tf.float32,shape=(None,1),name='y_data')
#定义向前传播过程
a=tf.matmul(x_data,w1)
y=tf.matmul(a,w2)

#定义损失函数和向前传播算法
y=tf.sigmoid(y)
cross_entropy=-tf.reduce_mean(y_data*tf.log(tf.clip_by_value(y,1e-10,1.0)))
train_step=tf.train.AdamOptimizer(0.001).minimize(cross_entropy)
#生成模拟数据集
rdm=RandomState(1)
dataset_size=128

X=rdm.rand(dataset_size,2)

Y=[[int (x1+x2<1)] for(x1,x2) in X]
with tf.Session() as ss:
    init=tf.global_variables_initializer()
    ss.run(init)
    print(ss.run(w1))
    print(ss.run(w2))

    STEPS=5000
    for i in range(STEPS):
        start=(i*batch_size)%dataset_size
        end=min(start+batch_size,dataset_size)
        ss.run(train_step,feed_dict={x_data:X[start:end],y_data:Y[start:end]})
        if(i%1000==0):
            total_cross_entropy=ss.run(cross_entropy,feed_dict={x_data:X[start:end],y_data:Y[start:end]})
            print("After %d training steps,cross entropy is %g "%(i,total_cross_entropy))

        print(ss.run(w1))
        print(ss.run(w2))







