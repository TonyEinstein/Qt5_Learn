#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/6 11:07
# file: 窗口跳转.py
# author: chenruhai
# email: ruhai.chen@qq.com


from PySide2 import QtWidgets
import sys

class Window2(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('窗口2')

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        button = QtWidgets.QPushButton('按钮2：：打开窗口1')
        button.clicked.connect(self.open_new_window)

        grid = QtWidgets.QGridLayout(centralWidget)
        grid.addWidget(button)

    def open_new_window(self):
        # 实例化另外一个窗口
        self.mainw =MainWindow()
        # 显示新窗口
        self.mainw.show()
        # 关闭自己
        self.close()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('窗口1')

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        button = QtWidgets.QPushButton('按钮1：打开窗口2')
        button.clicked.connect(self.open_new_window)

        grid = QtWidgets.QGridLayout(centralWidget)
        grid.addWidget(button)

    def open_new_window(self):
        # 实例化另外一个窗口
        self.window2 = Window2()
        # 显示新窗口
        self.window2.show()
        # 关闭自己
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

"""
如果经常要在两个窗口来回跳转，可以使用 hide() 方法 隐藏窗口， 而不是 closes() 方法关闭窗口。
这样还有一个好处：被隐藏的窗口再次显示时，原来的操作内容还保存着，不会消失。
"""