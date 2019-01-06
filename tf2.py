import tensorflow as tf
import numpy as np


# 创建一个常量op,产生一个1*2矩阵. 这个op被作为一个节点
# 加到默认图中

# 构造器的返回值代表常量op的返回值.
matrix1 = tf.constant([[3., 3.]])


# 创建另外一个常量op，产生一个2*1的矩阵
matrix2 = tf.constant([[2.],[2.]])

# 创建一个矩阵乘法matmul op, 把两个矩阵输入进去并返回结果
product = tf.matmul(matrix1, matrix2)

# 启动默认图
sess = tf.Session()

# 调用 sess 的 'run()' 方法来执行矩阵乘法 op, 传入 'product' 作为该方法的参数. 
# 上面提到, 'product' 代表了矩阵乘法 op 的输出, 传入它是向方法表明, 我们希望取回
# 矩阵乘法 op 的输出.
#
# 整个执行过程是自动化的, 会话负责传递 op 所需的全部输入. op 通常是并发执行的.
# 
# 函数调用 'run(product)' 触发了图中三个 op (两个常量 op 和一个矩阵乘法 op) 的执行.
#
# 返回值 'result' 是一个 numpy `ndarray` 对象.
result = sess.run(product)
print(result)

# 任务结束，关闭会话
sess.close()