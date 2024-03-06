#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/6 14:53
# file: TextBrowser文本浏览框.py
# author: chenruhai
# email: ruhai.chen@qq.com
from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtWidgets

# class Window(QtWidgets.QWidget):
#     def __init__(self):
#         label_path = QtWidgets.QLabel('初始内容', self)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义,从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了,比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/标签ui.ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('标签示例')
        # 1.创建标签对象
        # label_path = QtWidgets.QLabel('初始内容', self)

        # 2.改变文本：使用 setText 方法来改变 标签文本内容
        self.ui.label_2.setText("改变了文本")
        # 3. 获取文本：使用 text 方法来获取 标签文本内容
        rst = self.ui.label_3.text()
        print(rst)

        """
        4.显示图片：【显示不出，原因不详，反正不经常用这个】
        可以在 Qt Designer上 属性编辑器 QLabel 栏 的 pixmap 属性设置中选择图片文件指定。
        QLabel可以用来显示图片，有时一个图片可以让界面好看很多
        """
        # new_size = self.ui.label_4.scaled(20,20)
        # self.ui.label_4.setPixmap(new_size)

    def handleChanged(self):
        print("光标位置在改变，包括编辑位置和新增内容都是在改变哦")
    def handleTextChange(self):
        print("多行纯文本框 文本被修改，这里不会有返回值作为信号函数的参数；每编辑一次会执行一次该函数")

app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()



"""
QTextBrowser 是 只能查看文本 控件。
通常用来显示一些操作日志信息、或者不需要用户编辑的大段文本内容。
"""