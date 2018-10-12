import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#导入数据集
mnist=input_data.read_data_sets("e://MNIST_data",one_hot=True)
mnist=input_data.read_data_sets("e://MNIST_data",one_hot=True)
#设置batch
batch_size=100
n_batch=mnist.train.num_examples//batch_size
batch_size=100
n_batch=mnist.train.num_examples//batch_size
#初始化权值
def weight_variable(shape):
    initial=tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)
def Weight_variable(shape):
    initial=tf.truncated_normal(shape,stddev=0.1)#生成一个截断正态分布
    return tf.Variable(initial)
#初始化偏置值
def bias_variable(shape):
    initial=tf.constant(0.1,shape=shape)
def bias_variable(shape):
    initial=tf.constant(0.1,shape=shape)
    return tf.Variable(initial)
#卷积层
'''x:input tensor of shape [batch,height,width,channels]
   W:filter/kenel [height1,width1,channels,num]
   strides步长，strides[0],[3]默认为1，中间为自己设置
   padding：填充模式，same原图大小填充 valid 无填充
'''
def conv2d(x,w):
    return tf.nn.conv2d(x,w,strides=[1,1,1,1],padding='SAME')
def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')
#池化层
def pooling(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
def pooling(x):
   return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

#定义两个placeholder盛放训练集
x=tf.placeholder(tf.float32,[None,784])
y=tf.placeholder(tf.float32,[None,10])

x=tf.placeholder(tf.float32,[None,784])
y=tf.placeholder(tf.float32,[None,10])
#改变图片的格式为4维,1表示为一维度，黑白图片
x_image=tf.reshape(x,[-1,28,28,1])
x_image=tf.reshape(x,[-1,28,28,1])
#初始化第一个卷积(filter)和偏置
w1=weight_variable([5,5,1,32])
b1=bias_variable(32)
W_conv1=Weight_variable([5,5,1,32])
b_conv1=bias_variable([32])
#进行第一次卷积操作,是一个立方体
h1=tf.nn.relu(conv2d(x_image,w1)+b1)
p1=pooling(h1)
h_conv1=tf.nn.relu(conv2d(x_image,W_conv1)+b_conv1)
h_pool1=pooling(h_conv1)

#初始化第二个卷积和偏置
w2=weight_variable([5,5,32,64])
b2=bias_variable([64])
W_conv2=Weight_variable([5,5,32,64])
b_conv2=bias_variable([64])

#进行第二次卷积操作,是一个立方体
h2=tf.nn.relu(conv2d(p1,w2)+b2)
p2=pooling(h2)
h_conv2=tf.nn.relu(conv2d(h_pool1,W_conv2)+b_conv2)
h_pool2=pooling(h_conv2)

#初始化第一层全连接权值
W_fc1=Weight_variable([7*7*64,1024])
b_fc1=bias_variable([1024])
#把池化层2的输出扁平成一维
h_pool2_flat=tf.reshape(h_pool2,[-1,7*7*64])
#得到第一个全连接层的输出
h_fc1=tf.nn.relu(tf.matmul(h_pool2_flat,W_fc1)+b_fc1)

keep_prob=tf.placeholder(tf.float32)
h_fc1_drop=tf.nn.dropout(h_fc1,keep_prob)

#初始化第二层全连接权值
W_fc2=Weight_variable([1024,10])
b_fc2=bias_variable([10])

prediction=tf.nn.softmax(tf.matmul(h_fc1_drop,W_fc2)+b_fc2)

#定义交叉熵
cross_entropy=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))

train_step=tf.train.GradientDescentOptimizer(0.4).minimize(cross_entropy)
correct_pre=tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))

#求准确率
accuracy=tf.reduce_mean(tf.cast(correct_pre,tf.float32))

with tf.Session() as s:
    s.run(tf.global_variables_initializer())
    for epoch in range(2):
        batch_xs,batch_ys=mnist.train.next_batch(batch_size)
        s.run(train_step,feed_dict={x:batch_xs,y:batch_ys,keep_prob:0.7})
    acc=s.run(accuracy,feed_dict={x:mnist.train.images,y:mnist.train.labels,keep_prob:1.0})
    print("轮次：%s, 正确率: %s"%(epoch,acc))
