"""
绘制小猪佩奇
"""
from turtle import *

'''
pycharm有个bug 当通过 from  import * 这种方式引入标准库的模块时 由于不能识别__ALL__ 
事实上是pycharm默认该项目的根目录为source目录，
所以import使用绝对路径而不是相对路径的话，就会从项目的根目录中查找，
而不是我们希望的其中的/src目录，所以import不成功。

解决办法:
1 改成相对路径 
from ...package import * 
第一个.表示当前目录，后面的每一个’.’表示上一层目录。用相对目录可以保证import成功，但是不建议这种写法，因为如果当前这个文件要移动到其他包的话，就要改很多地方了，当然，使用相对路径表示可以随意更改包名，只要保证

2在pycharm中设置source路径

file–>setting–>project:server–>project structure

将放package的文件夹设置为source，这样import的模块类等，就是通过这些source文件夹作为根路径来查找，也就是在这些source文件夹中查找import的东西。 

3 https://stackoverflow.com/questions/25588642/pycharm-false-syntax-error-using-turtle
添加# noinspection PyUnresolvedReferences
'''


# noinspection PyUnresolvedReferences
def nose(x, y):
    """画鼻子"""
    penup()
    # 将海龟移动到指定的坐标
    goto(x, y)
    pendown()
    # 设置海龟的方向（0-东、90-北、180-西、270-南）
    setheading(-30)
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            # 向左转3度
            left(3)
            # 向前走
            forward(a)
        else:
            a = a - 0.08
            left(3)
            forward(a)
    end_fill()
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    # 设置画笔的颜色(红, 绿, 蓝)
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()
    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()


# noinspection PyUnresolvedReferences
def head(x, y):
    """画头"""
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)
    penup()
    goto(-100, 100)
    pendown()
    setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3)  # 向左转3度
            fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()


# noinspection PyUnresolvedReferences
def ears(x, y):
    """画耳朵"""
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()
    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()


# noinspection PyUnresolvedReferences
def eyes(x, y):
    """画眼睛"""
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
    color((255, 155, 192), "white")
    penup()
    seth(90)
    forward(-25)
    seth(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()


# noinspection PyUnresolvedReferences
def cheek(x, y):
    """画脸颊"""
    color((255, 155, 192))
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


# noinspection PyUnresolvedReferences
def mouth(x, y):
    """画嘴巴"""
    color(239, 69, 19)
    penup()
    goto(x, y)
    pendown()
    setheading(-80)
    circle(30, 40)
    circle(40, 80)


# noinspection PyUnresolvedReferences
def setting():
    """设置参数"""
    pensize(4)
    # 隐藏海龟
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(10)


def main():
    """主函数"""
    setting()
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes(0, 140)
    cheek(80, 10)
    mouth(-20, 30)
    done()


if __name__ == '__main__':
    main()
