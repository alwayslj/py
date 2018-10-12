import tensorflow as tf
v=tf.constant([1.0,2.0,3.0])
v1=tf.constant([[1.0,2.0],[3.0,4.0]])
v1=tf.constant([[5.0,6.0],[7.0,8.0]])
with tf.Session() as ss:

    print(ss.run(tf.log(v).eval()))