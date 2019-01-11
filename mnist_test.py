import tensorflow as tf


# 占位符，把图片平展成784维的向量，用二维的浮点数来表示，None指的第一个维度可以是任何长度
x=tf.placeholder("float", [None, 784])

 # 一个Variable代表一个可修改的张量，存在在TensorFlow的用于描述交互性操作的图中
w=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))
# 实现模型
y=tf.nn.softmax(tf.matmul(x,w) + b)