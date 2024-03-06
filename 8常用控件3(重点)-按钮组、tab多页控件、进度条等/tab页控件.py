#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/6 15:55
# file: ComboBox组合选择框.py
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
        self.ui = QUiLoader().load('ui/tab页控件.ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('tab页控件示例，所有操作都在设计师里面')
        """
        如果我们要在tab页上布局， 你可能会在对象查看器总直接右键点击该tab，可以你会发现 右键菜单里面没有布局项。
        这是 Qt designer 非常坑爹的地方，我当时足足花了一个小时才找到方法。
            1.首先需要你在tab页上添加一个控件
            2.然后点击 在对象查看器 右键点击上层 TabWidget ，这时，你就会发现有布局菜单了
        """

app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()