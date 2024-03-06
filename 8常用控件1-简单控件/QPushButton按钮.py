#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/6 11:37
# file: QPushButton按钮.py
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
        self.ui = QUiLoader().load('ui/按钮ui.ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('按钮操作')
        """
        按钮------------------------------------------------------
        """
        # 点击：当按钮被点击就会发出 clicked 信号，可以这样指定处理该信号的函数
        self.ui.pushButton.clicked.connect(self.handleCalc)
        self.i = 0
        #改变文本
        text = "改变文本"
        self.ui.pushButton_2.setText(text)

        # 禁用启用：禁用后，该控件不再处理用户操作
        self.ui.pushButton_3.setEnabled(False)
        # self.ui.pushButton_3.setEnabled(True)

        # 设置图标
        # 设置图标
        self.ui.pushButton_4.setIcon(QIcon('ui/logo.png'))
        # 设置图标大小
        self.ui.pushButton_4.setIconSize(QSize(50, 50))

    def handleCalc(self):
        self.i += 1
        self.ui.pushButton.setText("被点击操作在执行中,{}".format(self.i))
        print("被点击的信号 次数{}".format(self.i))



app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()
