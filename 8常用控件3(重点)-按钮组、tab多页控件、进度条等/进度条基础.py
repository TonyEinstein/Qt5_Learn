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
        self.ui = QUiLoader().load('ui/进度条.ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('进度条示例，所有操作都在设计师里面')
        """
        进度条也是一个常用的控件，当程序需要做一件比较耗费时间的任务（比如统计数据，下载文件等）时，可以用来向用户指示操作的进度。
        而且有了进度显示，用户就知道应用程序仍在运行，并没有出问题。
        QProgressBar进度条把每个进度称之为一个step（步骤）。
        """
        self.ui.pushButton_start.clicked.connect(self.handleButtonClicked)
        # 使用reset()将进度条倒退到开头。也可以在信号槽里面绑定。
        self.ui.pushButton_clear.clicked.connect(self.ui.progressBar.reset())
    def handleButtonClicked(self):
        """
        有时候我们的任务没法知道完成了多少，比如下载一个未知大小的文件。
        这时，可以把range 范围都设置为0，这样，进度条会显示忙碌指示符，而不是显示进度百分比。
        :return:
        """
        # 通过它的 setRange 方法设定总的步骤个数
        self.ui.progressBar.setRange(0,10)
        # self.ui.progressBar.setRange(0,0)
        # 通过 setValue 方法，指定当前完成到了哪一步
        self.ui.progressBar.setValue(3)

app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()