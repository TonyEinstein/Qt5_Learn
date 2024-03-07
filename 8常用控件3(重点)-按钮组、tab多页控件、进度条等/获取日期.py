#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/7 9:04
# file: 获取日期.py
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
        self.ui = QUiLoader().load('ui/获取日期.ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('获取日期示例')
        """
        当用户点击日期时间控件并且选取了 日期和时间，后来程序要获取这个控件里面选定的日期时间，可以使用date方法获取日期对象。
        """
        # 返回 PySide2.QtCore.QDate 对象
        qdate = self.ui.dateEdit.date()

        # 可以转化为 指定格式的字符串
        dateStr = qdate.toString('yyyy-MM-dd')

        # 也可以获取年月日 对应的数字 ，比如日期是2020年5月2号
        year = qdate.year()  # 返回 2020
        month = qdate.month()  # 返回 5
        day = qdate.day()  # 返回 2
        print(dateStr)
        print(year,month,day)





app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()