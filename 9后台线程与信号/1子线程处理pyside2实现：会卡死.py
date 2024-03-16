#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/7 23:01
# file: 1子线程处理pyside2实现：会卡死.py
# author: chenruhai
# email: ruhai.chen@qq.com
from PySide2.QtWidgets import QApplication,QWidget,QPlainTextEdit,QProgressBar
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from time import sleep

class Start1(QWidget):
    def __init__(self):
        #-----动态加载ui文件-------#
        qtmp = QFile("ui/duoxiancheng.ui")# 导入Qt designer生成的界面ui文件
        qtmp.open(QFile.ReadOnly)
        qtmp.close()
        self.ui = QUiLoader().load(qtmp)

        self.ui.pushButton.clicked.connect(self.printFunc)  # 将pushButton按钮链接到打印函数

    #-------定义打印函数-----------#
    def printFunc(self):

        #-----读取输入的最大最小值--------#
        num_min = int(self.ui.lineEdit_min.text())
        num_max = int(self.ui.lineEdit_max.text())
        num = num_max - num_min + 1

        #---------打印函数的执行主体------------#
        for i in range(num):
            #哪怕不输出到文本框，只要点击了别的tab,那么就会卡死。
            #这里的卡死是：后台会执行到完毕然后主页面退出，后台执行的过程主页面是已经卡死了。
            # self.ui.plainTextEdit.appendPlainText(str(num_min))     # 输出到文本框
            self.ui.progressBar.setValue(int((i + 1) / num * 100))   # 给进度条赋值
            num_min += 1
            print(num_min)
            sleep(0.1)            # 休眠0.1秒，模拟实际运行时程序的耗时

if __name__ == '__main__':
    app = QApplication([])
    stats1 = Start1()
    stats1.ui.show()
    app.exec_()

"""
教程参考：https://blog.csdn.net/xhzc7/article/details/116702475
【非常推荐】
"""













