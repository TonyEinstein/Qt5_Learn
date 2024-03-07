#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/7 23:01
# file: 1子线程处理pyside2实现：会卡死.py
# author: chenruhai
# email: ruhai.chen@qq.com

from PySide2.QtWidgets import QApplication, QWidget, QPlainTextEdit, QProgressBar
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from threading import Thread
from PySide2.QtCore import Signal, QObject  # 导入信号类
from time import sleep


class MySignals(QObject):
    # 定义一种信号，因为有文本框和进度条两个类，此处要四个参数，类型分别是： QPlainTextEdit 、 QProgressBar、字符串和整形数字
    # 调用 emit方法发信号时，传入参数必须是这里指定的参数类型
    # 此处也可分开写两个函数，一个是文本框输出的，一个是给进度条赋值的
    text_print = Signal(QPlainTextEdit, QProgressBar, str, int)


class Start1(QWidget):
    def __init__(self):
        # -----动态加载ui文件-------#
        qtmp = QFile("ui/duoxiancheng.ui")
        qtmp.open(QFile.ReadOnly)
        qtmp.close()
        self.ui = QUiLoader().load(qtmp)

        self.ui.pushButton.clicked.connect(self.new_printFunc)

        self.ms = MySignals()  # 引入信号函数
        self.ms.text_print.connect(self.pF)  # 将信号传递给主程序中pF函数进行处理

    def new_printFunc(self):  # 新线程入口函数
        thread = Thread(target=self.printFunc)
        thread.start()

    def printFunc(self):  # 打印函数
        num_min = int(self.ui.lineEdit_min.text())
        num_max = int(self.ui.lineEdit_max.text())
        num = num_max - num_min + 1
        for i in range(num):
            # 此处不再直接操作主界面，而是发射信号给MySignals函数中的text_print，
            # 传递参数包括要操作哪个位置和要操作的内容
            self.ms.text_print.emit(self.ui.plainTextEdit, self.ui.progressBar, str(num_min), int((i + 1) / num * 100))
            num_min += 1
            sleep(0.1)

    # 接收到发来的信号，pt和pb就是要操作的位置self.ui.plainTextEdit和self.ui.progressBar，text和int1则是具体内容
    def pF(self, pt, pb, text, int1):
        pt.appendPlainText(text)
        pb.setValue(int1)


if __name__ == '__main__':
    app = QApplication([])
    stats1 = Start1()
    stats1.ui.show()
    app.exec_()

"""
教程参考：https://blog.csdn.net/xhzc7/article/details/116702475
【非常推荐】
"""













