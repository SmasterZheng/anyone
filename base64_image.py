import base64
import numpy as np
import cv2

def BaseTest():
	# 二进制读取图片
	imageFile=open('test.jpg', 'rb')
	text1=open('1.txt','w')
	text1.write(str(imageFile))
	text1.close()
	# base64转码
	img_64encode=base64.b64encode(imageFile.read())
	imageFile.close()
	# print(img_64encode)

	# base64解码
	img_64decode=base64.b64decode(img_64encode)
	text2=open('2.txt','w')
	text2.write(str(img_64decode))
	text2.close()

	# print(img_64decode)
	img_array=np.fromstring(img_64decode,np.uint8)
	img=cv2.imdecode(img_array,cv2.COLOR_BGR2RGB)

	cv2.imshow("img",img)
	cv2.waitKey()

if __name__ == '__main__':
	BaseTest()