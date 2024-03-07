#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/7 15:18
# file: 状态栏.py
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
        self.ui = QUiLoader().load('ui/菜单栏和菜单、工具栏、状态栏.ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('示例，所有操作都在设计师里面')



app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()





"""
态栏通常显示在窗口底部，对应的控件类型是: QStatusBar;
需要底部状态栏的，通常是 QMainWindow 类型的窗口, 用 Qt Designer 设计的Qt Designer， 会自带状态栏，缺省属性名称为 statusbar 。


要在状态栏显示文本信息，只需要调用 状态栏 QStatusBar 的 showMessage 方法，如下
self.ui.statusbar.showMessage(f'打开文件{filePath}')
"""