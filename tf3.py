import tensorflow as tf
import numpy as np


sess = tf.InteractiveSession()

x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0, 3.0])

# 使用初始化器 initializer op 的 run() 方法初始化 'x' 
x.initializer.run()

 # tf.mul,tf.sub,tf.neg 已经废弃分别可用tf.multiply, tf.subtract, tf.negative替代 
sub = tf.subtract(x, a)
print(sub.eval())