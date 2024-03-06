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
        self.ui = QUiLoader().load('ui/单选按钮和按钮组ui.ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('单选按钮示例')
        # 1.如果用户操作点击了按钮组 QButtonGroup 中的一个按钮， QButtonGroup 就会发出 buttonClicked 信号，可以这样指定处理该信号的函数。
        """
        然后，在处理函数中调用QButtonGroup对象的 checkedButton() 函数，返回值就是被选中的按钮对象。
        再调用这个返回的按钮对象的 text() 方法得到界面文本，就可以知道是哪个选项被选中了。
        """
        self.ui.buttonGroup_sex.buttonClicked.connect(self.handleButtonClicked)

    def handleButtonClicked(self):
        select_target = self.ui.buttonGroup_sex.checkedButton()
        print(select_target.text())


"""
QRadioButton 是单选按钮;
"""

"""
同一个父窗口 里面的多个单选按钮，只能选中一项。
如果你有多组单选按钮， 每组都应该有不同的父控件，或者不同的Layout。通常建议：多组单选按钮，放到不同的 按钮组 QButtonGroup 中。

也就是说要实现“同一个父窗口 里面的多个单选按钮，只能选中一项。”的需要，要么在Layout里面才添加单选按钮，要么新建不同的按钮组 QButtonGroup；要么使用groupbox。
"""

app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()