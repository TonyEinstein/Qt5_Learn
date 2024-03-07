#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/7 15:43
# file: 输入对话框.py
# author: chenruhai
# email: ruhai.chen@qq.com


from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QMessageBox, QInputDialog, QLineEdit


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义,从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了,比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/输入对话框.ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('示例，所有操作都在设计师里面')
        """
        QMessageBox 类可以用来弹出各种提示框;该类可以通过一系列静态方法，显示 如下弹出框。
        """
        # 1. 使用 critical 方法弹出错误报告。
        self.ui.pushButton.clicked.connect(self.input_onetext)
        self.ui.pushButton_2.clicked.connect(self.input_onetext)
        self.ui.pushButton_3.clicked.connect(self.input_moretext)
        self.ui.pushButton_4.clicked.connect(self.input_int)
        self.ui.pushButton_5.clicked.connect(self.input_select)

    def input_select(self):
        items = ["春天", "夏天", "秋天", "冬天"]

        item, ok = QInputDialog().getItem(self,
                                          "请选择",
                                          "季节:",
                                          items,
                                          0,
                                          False)
        if ok and item:
            self.ui.pushButton_5.setText(item)
            print("当前选项是：{}".format(item))
        else:
            print("用户取消选择")

    def input_int(self):
        # 返回值分别是输入数据 和 是否点击了 OK 按钮（True/False）
        title, okPressed = QInputDialog.getInt(
            self,
            "输入内容名称",
            "名称:",
            1
        )
        if not okPressed:
            print('你取消了输入')
        else:
            print("你进行了输入，内容是：{}".format(title))
    def input_moretext(self):
        # 返回值分别是输入数据 和 是否点击了 OK 按钮（True/False）
        title, okPressed = QInputDialog.getMultiLineText(
            self,
            "输入内容名称",
            "名称:",
            "此处为输入位置"
        )
        if not okPressed:
            print('你取消了输入')
        else:
            print("你进行了输入，内容是：{}".format(title))
    def input_onetext(self):
        # 返回值分别是输入数据 和 是否点击了 OK 按钮（True/False）
        title, okPressed = QInputDialog.getText(
            self,
            "输入目录名称",
            "名称:",
            QLineEdit.Normal,
            "此处为输入位置"
        )
        if not okPressed:
            print('你取消了输入')
        else:
            print("你进行了输入，内容是：{}".format(title))

app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()

"""
常用的方法有：
getText弹出对话框，让用户输入 单行文本
getMultiLineText弹出对话框，让用户输入 多行文本
getInt弹出对话框，让用户输入 整数
getItem弹出对话框，让用户选择 选项
"""