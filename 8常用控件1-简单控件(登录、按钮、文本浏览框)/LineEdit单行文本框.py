#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/6 12:03
# file: LineEdit单行文本框.py
# author: chenruhai
# email: ruhai.chen@qq.com



import sys
import pandas as pd
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication,QMainWindow
from PySide2.QtUiTools import QUiLoader



class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义,从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了,比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/单行文本框ui.ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('单行文本框操作')
        """
        1.信号：文本被修改。
        当文本框中的内容被键盘编辑，被点击就会发出 textChanged 信号，可以这样指定处理该信号的函数
        Qt在调用这个信号处理函数时，传入的参数就是 文本框目前的内容字符串。
        """
        self.ui.lineEdit.textChanged.connect(self.handleTextChange)

        """
        2.信号：按下回车键。
        当用户在文本框中任何时候按下回车键，就会发出 returnPressed 信号。
        有时我们需要处理这种情况，比如登录界面，用户输完密码直接按回车键就进行登录处理，比再用鼠标点击登录按钮快捷的多。可以指定处理 returnPressed 信号。
        """
        self.ui.lineEdit_2.returnPressed.connect(self.onLogin)

        # 3.获取文本：通过 text 方法获取编辑框内的文本内容，比如
        print(self.ui.lineEdit_3.text())

        # 4.设置提示：通过 setPlaceholderText 方法可以设置提示文本内容，比如
        self.ui.lineEdit_4.setPlaceholderText('设置提示：请在这里输入URL')

        # 5.设置文本;通过 setText 方法设置编辑框内的文本内容为参数里面的文本字符串;原来的所有内容会被清除。
        self.ui.lineEdit_5.setText('设置文本（会覆盖掉原来的）')

        # 6.清除所有文本:clear 方法可以清除编辑框内所有的文本内容
        self.ui.lineEdit_6.clear()

        # 拷贝和粘贴文本
        self.ui.lineEdit_7.copy()

        self.ui.lineEdit_8.paste()


    def onLogin(self):
        print("模拟登录的响应，此处可更换为 跳转到登录页面")


    def handleTextChange(self,text):
        print("从文本框接收到的内容：",text)





app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()