#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/7 1:25
# file: 数值(数字)输入框.py.py
# author: chenruhai
# email: ruhai.chen@qq.com

import time

from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义,从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了,比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/数值(数字)输入框.ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('数字输入框示例')
        #1.获取数字；通过 value 方法获取编辑框内的文本内容；注意：返回的是整数对象，不是字符串。
        number = self.ui.spinBox.value()
        print(number)

        #2.设置数字;通过 setValue 方法可以设置提示文本内容（也不算是提示，而是直接赋值了）。
        self.ui.spinBox_2.setValue(79)

app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()