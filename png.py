import matplotlib.pyplot as plt
import tensorflow as tf
#读取图像原始数据
image_raw_data=tf.gfile.FastGFile("E://cat.png",'rb').read()
with tf.Session() as s:
    img_data=tf.image.decode_jpeg(image_raw_data)
    print(img_data.eval())
    plt.imshow(img_data.eval())
    plt.show()