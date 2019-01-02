from tkinter import *

window = Tk()
window.title('复制一下，你就知道')
window.geometry('600x400')

thelabel=Entry(window,show=None,width=30)
thelabel.pack()
# 点击按钮1执行的函数
def insert_point():
	print('aaaa')

# 设置按钮1
button1=Button(window,text='我是按钮',command=insert_point)
button1.pack()
mainloop()
