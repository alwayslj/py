import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
'''m1=tf.constant([[3,3]])
m2=tf.constant([[2],[3]])
product=tf.matmul(m1,m2)
with tf.Session() as s:
    result=s.run(product)
    print(result)

#变量的使用
n=tf.Variable([[2,3]])
a=tf.constant([[3,3]])
r1=tf.subtract(n,a)
#变量初始化
init=tf.global_variables_initializer()

with tf.Session() as ss:
    ss.run(init)
    r=ss.run(r1)
    print(r)



state=tf.Variable(0,name='counter')
new_value=tf.add(state,1)
update=tf.assign(state,new_value)
init=tf.global_variables_initializer()
with tf.Session() as sss:
    sss.run(init)
    print(sss.run(state))
    for i in range(5):
        print(sss.run(update))
m1=tf.constant(2)
m2=tf.constant(5)
m3=tf.constant(3)
x1=tf.add(m1,m2)
x2=tf.multiply(x1,m3)
with tf.Session() as s:
    print(s.run([x1,x2]))
input1=tf.placeholder(tf.float32)
input2=tf.placeholder(tf.float32)
output=tf.multiply(input1,input2)
with tf.Session() as s:
    print(s.run(output,feed_dict={input1:1.0,input2:3.0}))
import numpy as np
x_data=np.random.rand(100)
y_data=0.1*x_data+0.2

#构造一个线性模型
b=tf.Variable(0.)
k=tf.Variable(0.)
y=k*x_data+b

#构造二次代价函数（loss函数）
loss=tf.reduce_mean(tf.square(y-y_data))
optimizer=tf.train.GradientDescentOptimizer(0.2)
train=optimizer.minimize(loss)
init=tf.global_variables_initializer()
with tf.Session() as s:
    s.run(init)
    for step in range(401):
        s.run(train)
        if(step%20==0):
            print(step,s.run([k,b]))

x_data=np.random.rand(100)
y_data=x_data*0.1+0.2

#构造一个模型
b=tf.Variable(0.)
k=tf.Variable(0.)
y=k*x_data+b

#定义一个二次代价函数
loss=tf.reduce_mean(tf.square(y-y_data))
#利用梯度下降法不断改变变量k和b
optimizer=tf.train.GradientDescentOptimizer(0.2)
train=optimizer.minimize(loss)
init=tf.global_variables_initializer()

with tf.Session() as s:
    s.run(init)
    for step in range(200):
        s.run(train)
        if(step%20==0):
            print(step,s.run([k,b]))
#====================================================回归的例子
x_data=np.linspace(-0.5,0,5,200)[:,np.newaxis]
noise=np.random.normal(0,0.02,x_data,shape)
y_data=np.square(x_data)+noise

x=tf.placeholder(tf.float32)
y=tf.placeholder(tf.float32)

'''
#==================================
import tensorflow as tf
g1=tf.Graph()
with g1.as_default():
    v=tf.get_variable(
        "v",initializer=tf.zeros_initializer()(shape=[1]))
with tf.Session(graph=g1) as ss:
    tf.global_variables_initializer().run()
    with tf.variable_scope("",reuse=True):
        print(ss.run(tf.get_variable("v")))

