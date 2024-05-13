#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/6 15:55
# file: ComboBox组合选择框.py
# author: chenruhai
# email: ruhai.chen@qq.com
import time

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义,从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了,比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/组合选择框ui.ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('组合选择框示例')

        """
        1.信号：选项改变
        如果用户操作修改了QComboBox中的选项就会发出 currentIndexChanged 信号，可以这样指定处理该信号的函数
        """
        self.ui.comboBox.currentIndexChanged.connect(self.handleSelectionChange)
        # choose = self.ui.comboBox.currentIndexChanged.connect(self.handleSelectionChange)#这种是错误的，不建议
        # 2.添加一个选项： 代码中可以使用 addItem 方法来添加一个选项到 末尾 ，参数就是选项文本
        self.ui.comboBox.addItem('send')
        # 3.添加多个选项：代码中可以使用 addItems 方法来添加多个选项到 末尾，参数是包含了多个选项文本的列表。
        self.ui.comboBox_2.addItems(['svm模型','逻辑回归模型','KNN','K聚类'])

        # 4.清空选择框内的所有选项
        self.ui.comboBox_3.clear()
        self.ui.comboBox_3.addItems(['svm模型', '逻辑回归模型', 'KNN', 'K聚类'])

        # 5. 获取当前选项文本;代码中可以使用 currentText 方法来获取当前 选中的选项 的文本。需要调用方法返回，不能直接打印
        # print(self.ui.comboBox_2.currentText())
        # 下面这种方式是错误的，不能够在handleSelectionChange接收返回值后在此处直接打印
        # print(choose)


    def handleSelectionChange(self):
        # 代码中可以使用 currentText 方法来获取当前 选中的选项 的文本
        types = self.ui.comboBox.currentText()
        print("选择了当前模式：{}".format(types))
        # return types

app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()