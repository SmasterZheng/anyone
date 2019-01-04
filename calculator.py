from tkinter import *
from tkinter import ttk
import base64
from qq import img
import os


# 将图标icon文件转化成编码形式
# open_icon = open('icon.ico','rb')
# b64str = base64.b64encode(open_icon.read())
# open_icon.close()
# write_data = "img = '%s'" % b64str.decode()
# f=open("icon.py","w+")
# f.write(write_data)
# f.close()


calculator = Tk()
# 将图标显示出来
# tmp = open('tmp.ico','wb+')
# tmp.write(base64.b64decode(img))
# tmp.close()
# calculator.iconbitmap('16.ico')
# os.remove("tmp.ico")
calculator.title('简易计算器1.0.1')
calculator.geometry('380x292+500+250')
# 限制边框不能变
calculator.resizable(False, False)
# 显示框样式
show = ttk.Frame(calculator, padding="0 0 12 0")
show.grid(column=0, row=0, columnspan=2)
# 第一行按钮样式
first = ttk.Frame(calculator, padding="0 0 3 0")
first.grid(column=0, row=1, sticky=(N, W, E, S))
# 第二行按钮样式
second = ttk.Frame(calculator, padding="0 0 3 0")
second.grid(column=0, row=2, sticky=(N, W, E, S))
# 第三行按钮样式
third = ttk.Frame(calculator, padding="0 0 3 0")
third.grid(column=0, row=3, sticky=(N, W, E, S))
# 第四行按钮样式
fourth = ttk.Frame(calculator, padding="0 0 3 0")
fourth.grid(column=0, row=4, sticky=(N, W, E, S))
# 等于号的样式
equ = ttk.Frame(calculator, padding="0 10 12 0")
equ.grid(column=1, row=2, rowspan=3, sticky=(N, W, E, S))
# 清除的样式
clear = ttk.Frame(calculator, padding="0 0 12 0")
clear.grid(column=1, row=1, sticky=(N, W, E, S))
# 运算符及点
operator = ['+', '-', '*', '/', '.']
# 实现计算器功能部分
# 数字部分


def one():
    text.insert('end', '1')


def two():
    text.insert('end', '2')


def three():
    text.insert('end', '3')


def four():
    text.insert('end', '4')


def five():
    text.insert('end', '5')


def six():
    text.insert('end', '6')


def seven():
    text.insert('end', '7')


def eight():
    text.insert('end', '8')


def nine():
    text.insert('end', '9')


def zero():
    text.insert('end', '0')


# 加
def Add():
    # text.insert('end', '+')
    i = str(text.get(1.0, END)[-2])
    if i in operator:
        pass
    else:
        text.insert('end', '+')


# 减
def Sup():
    i = str(text.get(1.0, END)[-2])
    if i in operator:
        pass
    else:
        text.insert('end', '-')


# 乘
def Mult():
    i = str(text.get(1.0, END)[-2])
    if i in operator:
        pass
    else:
        text.insert('end', '*')


# 除
def Div():

    i = str(text.get(1.0, END)[-2])
    if i in operator:
        pass
    else:
        text.insert('end', '/')


# 清除键的执行函数
def clear_all():
    text.delete(0.0, END)


# 删除键的执行函数
def del_one():
    # a=str(text.get(1.0,END))
    # print(a[-2])
    text.delete((1.0, '2.0')[-2])


def point():
    i = str(text.get(1.0, END)[-2])
    if i in operator:
        pass
    else:
        text.insert('end', '.')

        
# 等号利用eval函数直接计算
def count():
    result = str(eval(text.get(1.0, END)))
    text.insert('end', '\n' + result)

# 计算器显示部分
text = Text(show, height=2, font=('Arial', 20), width=25)
text.pack()
# 计算器第一行的按钮
button1 = Button(first, text='1', font=('Arial', 20), width=4, command=one)
button1.pack(side=LEFT)
button2 = Button(first, text='2', font=('Arial', 20), width=4, command=two)
button2.pack(side=LEFT)
button3 = Button(first, text='3', font=('Arial', 20), width=4, command=three)
button3.pack(side=LEFT)
add = Button(first, text='+', font=('Arial', 20), width=4, command=Add)
add.pack(side=LEFT)
# 清除键
crear = Button(clear, text='C', font=('Arial', 20), width=4, command=clear_all)
crear.pack(side=LEFT)
# 计算器第二行的按钮
button4 = Button(second, text='4', font=('Arial', 20), width=4, command=four)
button4.pack(side=LEFT)
button5 = Button(second, text='5', font=('Arial', 20), width=4, command=five)
button5.pack(side=LEFT)
button6 = Button(second, text='6', font=('Arial', 20), width=4, command=six)
button6.pack(side=LEFT)
sub = Button(second, text='-', font=('Arial', 20), width=4, command=Sup)
sub.pack(side=LEFT)
# 等于号的按钮
equal = Button(equ, text='=', font=('Arial', 20),
               width=4, height=4, command=count)
equal.pack()
# 计算器第三行的按钮
button7 = Button(third, text='7', font=('Arial', 20), width=4, command=seven)
button7.pack(side=LEFT)
button8 = Button(third, text='8', font=('Arial', 20), width=4, command=eight)
button8.pack(side=LEFT)
button9 = Button(third, text='9', font=('Arial', 20), width=4, command=nine)
button9.pack(side=LEFT)
mult = Button(third, text='*', font=('Arial', 20), width=4, command=Mult)
mult.pack(side=LEFT)
# 计算器第四行的按钮
dele = Button(fourth, text='←', font=('Arial', 20), width=4, command=del_one)
dele.pack(side=LEFT)
button0 = Button(fourth, text='0', font=('Arial', 20), width=4, command=zero)
button0.pack(side=LEFT)
spot = Button(fourth, text='.', font=('Arial', 20), width=4, command=point)
spot.pack(side=LEFT)
div = Button(fourth, text='/', font=('Arial', 20), width=4, command=Div)
div.pack(side=LEFT)


# 将窗口显示出来
mainloop()
