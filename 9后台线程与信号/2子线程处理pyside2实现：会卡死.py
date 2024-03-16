#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/7 23:01
# file: 1子线程处理pyside2实现：会卡死.py
# author: chenruhai
# email: ruhai.chen@qq.com

from PySide2.QtWidgets import QApplication,QWidget,QPlainTextEdit,QProgressBar
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from threading import Thread  # 导入thread
from time import sleep

class Start1(QWidget):
    def __init__(self):
        #-----动态加载ui文件-------#
        qtmp = QFile("ui/duoxiancheng.ui")
        qtmp.open(QFile.ReadOnly)
        qtmp.close()
        self.ui = QUiLoader().load(qtmp)

        self.ui.pushButton.clicked.connect(self.new_printFunc)  # 将pushButton按钮链接到新线程函数

    #-------定义打印函数-----------#
    def printFunc(self):

        #-----读取输入的最大最小值--------#
        num_min = int(self.ui.lineEdit_min.text())
        num_max = int(self.ui.lineEdit_max.text())
        num = num_max - num_min + 1

        #---------打印函数的执行主体------------#
        for i in range(num):
            # 多次点击开始就出现问题。
            # self.ui.plainTextEdit.appendPlainText(str(num_min))     # 输出到文本框
            self.ui.progressBar.setValue(int((i + 1) / num * 100))   # 给进度条赋值
            num_min += 1
            print(num_min)
            sleep(0.01)            # 休眠0.1秒，模拟实际运行时程序的耗时

    #-------创建新线程函数------#
    def new_printFunc(self):
        thread = Thread(target=self.printFunc)  #此处省略了参数args=('参数1', '参数2')，仅指定了新线程入口函数（即我们定义好的打印函数）
        thread.start() # 开启新线程

if __name__ == '__main__':
    app = QApplication([])
    stats1 = Start1()
    stats1.ui.show()
    app.exec_()





"""
教程参考：https://blog.csdn.net/xhzc7/article/details/116702475
【非常推荐】
"""













