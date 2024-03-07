#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/8 0:40
# file: 子线程发信号更新界面.py
# author: chenruhai
# email: ruhai.chen@qq.com

from PySide2.QtWidgets import QApplication, QTextBrowser
from PySide2.QtUiTools import QUiLoader
from threading import Thread

from PySide2.QtCore import Signal,QObject

# 自定义信号源对象类型，一定要继承自 QObject
class MySignals(QObject):

    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    text_print = Signal(QTextBrowser,str)

    # 还可以定义其他种类的信号
    update_table = Signal(str)

# 实例化
global_ms = MySignals()

class Stats:

    def __init__(self):
        self.ui = QUiLoader().load('main.ui')
        """
        因为不知道这个东西长啥样所以这里的代码只拿来理解，没有main.ui配合运行。有会的麻烦可以补充一下提交requests。
        或者可以去看3子线程处理pyside2实现：正常-子线程发信号更新界面，这个讲的很清楚。
        """
        # 自定义信号的处理函数
        global_ms.text_print.connect(self.printToGui)


    def printToGui(self,fb,text):
        fb.append(str(text))
        fb.ensureCursorVisible()

    def task1(self):
        def threadFunc():
            # 通过Signal 的 emit 触发执行 主线程里面的处理函数
            # emit参数和定义Signal的数量、类型必须一致
            global_ms.text_print.emit(self.ui.infoBox1, '输出内容')

        thread = Thread(target = threadFunc )
        thread.start()

    def task2(self):
        def threadFunc():
            global_ms.text_print.emit(self.ui.infoBox2, '输出内容')

        thread = Thread(target=threadFunc)
        thread.start()

if __name__ == '__main__':
    app = QApplication([])
    stats1 = Stats()
    stats1.ui.show()
    app.exec_()

"""
Qt建议： 只在主线程中操作界面 。
"""

"""
在另外一个线程直接操作界面，可能会导致意想不到的问题，比如：输出显示不全，甚至程序崩溃。
但是，我们确实经常需要在子线程中 更新界面。比如子线程是个爬虫，爬取到数据显示在界面上。怎么办呢？


这时，推荐的方法是使用信号。
前面我们曾经看到过 各种 Qt 控件可以发出信号，比如 被点击、被输入等。我们也可以自定义类，只要这个类继承QObject类，就能发出自己定义的各种Qt信号，
具体做法如下：
自定义一个Qt 的 QObject类，里面封装一些自定义的 Signal信号,一种信号定义为 该类的 一个 静态属性，值为Signal 实例对象即可。
可以定义 多个 Signal静态属性，对应这种类型的对象可以发出的 多种 信号。
注意：Signal实例对象的初始化参数指定的类型，就是 发出信号对象时，传递的参数数据类型。因为Qt底层是C++开发的，必须指定类型。
(1)定义主线程执行的函数处理Signal信号（通过connect方法）;
(2)在新线程需要操作界面的时候，就通过自定义对象 发出 信号;通过该信号对象的 emit方法发出信号， emit方法的参数 传递必要的数据。参数类型 遵循 定义Signal时，指定的类型。
(3)主线程信号处理函数，被触发执行，获取Signal里面的参数，执行必要的更新界面操作;
"""