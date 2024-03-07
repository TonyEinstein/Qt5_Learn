#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/7 15:27
# file: 提示框.py
# author: chenruhai
# email: ruhai.chen@qq.com
import time

from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QMessageBox


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义,从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了,比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/提示框使用.ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('示例，所有操作都在设计师里面')
        """
        QMessageBox 类可以用来弹出各种提示框;该类可以通过一系列静态方法，显示 如下弹出框。
        """
        # 1. 使用 critical 方法弹出错误报告。
        self.ui.pushButton.clicked.connect(self.mistake)
        self.ui.pushButton_2.clicked.connect(self.warning)
        self.ui.pushButton_3.clicked.connect(self.information)
        self.ui.pushButton_4.clicked.connect(self.ask_to_continue)

    def ask_to_continue(self):
        """
        确认是否继续进行下一步。
        使用 question 方法
        :return:
        """
        choice = QMessageBox.question(
            self.ui,
            '确认',
            '确定要删除本文件吗？')

        if choice == QMessageBox.Yes:
            print('你选择了yes')
        if choice == QMessageBox.No:
            print('你选择了no')
    def information(self):
        """
        对当前操作进行信息提示。
        使用 information 方法，也可以使用 about 方法；
        :return:
        """
        QMessageBox.about(
            self.ui,
            '操作成功',
            '请继续下一步操作')
        # QMessageBox.information(
        #     self.ui,
        #     '操作成功',
        #     '请继续下一步操作')

    def warning(self):
        """
        弹出警告。
        使用 warning 方法
        :return:
        """
        QMessageBox.warning(
            self.ui,
            '阅读太快',
            '阅读客户协议必须超过1分钟')
    def mistake(self):
        """
        弹出 错误报告。
        使用 critical 方法；
        :return:
        """
        QMessageBox.critical(
            self.ui,
            '错误',
            '请选择爬取数据存储路径！')


app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()