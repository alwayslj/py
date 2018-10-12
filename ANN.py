import tensorflow as tf
from numpy.random import RandomState
#定义batch的大小
batch_size=8
#定义神经网络参数
W1=tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
W2=tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))
#在shape上第一维度为None可以方便使用不同batch的大小。当数据集较小时比较方便测试，但当数据集很大时，需要分出batch批次
#否则可能会导致内存溢出
#定义两个placeholder
x=tf.placeholder(tf.float32,shape=(None,2),name='x-input')
y_=tf.placeholder(tf.float32,shape=(None,1),name='y-input')
#定义神经网络的向前传播过程

a=tf.matmul(x,W1)
prediction=tf.matmul(a,W2)

#定义损失函数
prediction=tf.sigmoid(prediction)
cross_entropy=-tf.reduce_mean(y_*tf.log(tf.clip_by_value(prediction,1e-10,1.0)))
#利用梯度下降法优化
train_step=tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

#通过随机数产生一个模拟数据集
rdm=RandomState(1)
dataset_size=128
X=rdm.rand(dataset_size,2)
Y=[[int (x1+x2<1)] for (x1,x2) in X]
#创建会话
with tf.Session() as ss:
    init=tf.global_variables_initializer()
    ss.run(init)
    ss.run(train_step)
    print(ss.run(W1))
    print(ss.run(W2))

#设定训练轮数
    STEPS=5000
    for i in range(STEPS):
        start=(i*batch_size)%dataset_size
        end=min(start+batch_size,dataset_size)

        #训练神经网络并更新参数
        ss.run(train_step,feed_dict={x:X[start:end],y_:Y[start:end]})
        if(i%1000==0):
            total_corss_entropy=ss.run(cross_entropy,feed_dict={x:X,y_:Y})
            print("轮数：%d, 交叉熵：%g"%(i,cross_entropy))

    print(ss.run(W1))
    print(ss.run(W2))
#======================================================================
