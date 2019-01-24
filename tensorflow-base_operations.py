# -*- coding: utf-8 -*-
import tensorflow as tf
import base64


def base64_decode_img(b64code):
    """
    :param b64code:输入为图像的base64编码字符串
    :return:
    """
    base64_tensor = tf.convert_to_tensor(b64code, dtype=tf.string)
    img_str = tf.decode_base64(base64_tensor) 
    #得到（width, height, channel）的图像tensor
    img = tf.image.decode_image(img_str, channels=3) 
    with tf.Session() as sess:
        img_value = sess.run([img])[0] #得到numpy array类型的数据
        print(img_value.shape)  


def BaseTest():
    # 二进制读取图片
    imageFile=open('test.jpg', 'rb')
    b64code=base64.b64encode(imageFile.read())
    imageFile.close()
    base64_decode_img(b64code)


def decode_base64(input, name=None):
  r"""Decode web-safe base64-encoded strings.

  Input may or may not have padding at the end. See EncodeBase64 for padding.
  Web-safe means that input must use - and _ instead of + and /.
  
https://blog.csdn.net/wangjian1204/article/details/80834593?utm_source=blogxgwz0
"""
if __name__ == '__main__':
    BaseTest()