import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
#载入数据
mnist=input_data.read_data_sets("e://MNIST_data",one_hot=True)
'''one_hot的意思是，一位有效编码。只有一个1'''
#定义batch
batch_size=100

#定义多少个batch
n_batch=mnist.train.num_examples//batch_size
#定义两个placeholder
x=tf.placeholder(tf.float32,[None,784])
y_=tf.placeholder(tf.float32,[None,10])

#创建简单的神经网络
W=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))

#预测值
prediction=tf.nn.softmax(tf.matmul(x,W)+b)
#定义代价函数
loss=tf.reduce_mean(tf.square(y_-prediction))
cross_entropy=-tf.reduce_mean(y_*tf.log(tf.clip_by_value(prediction,1e-10,1.0)))
#使用梯度下降
train_step=tf.train.AdamOptimizer(0.001).minimize(cross_entropy)
#初始化变量
init=tf.global_variables_initializer()
#测试准确率,放在一个boolen数组里
accuracy_pre=tf.equal(tf.argmax(y_,1),tf.argmax(prediction,1))

#求准确率
acc=tf.reduce_mean(tf.cast(accuracy_pre,tf.float32))

#开始进行训练,将所有训练集训练21轮
with tf.Session() as s:
    s.run(init)
    for i in range(21):
        for batch in range(n_batch):
            batch_xs,batch_ys=mnist.train.next_batch(batch_size)
            s.run(train_step,feed_dict={x:batch_xs,y_:batch_ys})
        accuracy=s.run(acc,feed_dict={x:mnist.train.images,y_:mnist.train.labels})
        print("轮数：%d,正确率：%s"%(i,accuracy))