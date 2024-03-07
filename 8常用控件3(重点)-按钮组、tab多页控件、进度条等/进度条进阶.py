#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/7 1:07
# file: 进度条进阶.py
# author: chenruhai
# email: ruhai.chen@qq.com

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QProgressBar,QMessageBox
from time import sleep
from threading import  Thread
from PySide2.QtCore import Signal,QObject

# 信号库
class SignalStore(QObject):
    # 定义一种信号，这个信号是一个整数类型的信号，可以用来在程序中发射（emit）整数数值。
    progress_update = Signal(int)
    # 还可以定义其他作用的信号

# 实例化
so = SignalStore()

class Stats():
    def __init__(self):

        # 连接信号到处理的slot函数
        so.progress_update.connect(self.setProgress)

        self.window = QMainWindow()
        self.window.resize(500, 400)#主界面大小
        self.window.move(300, 300)#主界面位置

        self.progressBar = QProgressBar(self.window)
        #设置百分比显示在中间，默认在右边
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.resize(300, 20)#进度条大小
        self.progressBar.move(80, 30)#位置
        # 进度是 0 - 5，
        self.progressBar.setRange(0,5)

        self.button = QPushButton('统计', self.window)
        self.button.move(80, 80)#位置
        self.button.clicked.connect(self.handleCalc)

        self.button2 = QPushButton('重置', self.window)
        self.button2.move(80, 150)  # 位置
        self.button2.clicked.connect(self.handleCalc2)

        # 统计进行中标记，不能同时做两个统计
        self.ongoing = False

    def handleCalc2(self):
        self.progressBar.reset()
        self.ongoing = False

    def handleCalc(self):
        def workerThreadFunc():
            self.ongoing = True
            for i in range(1,20):
                #进行一系列操作
                sleep(1)
                # 发出信息，通知主线程进行进度处理
                so.progress_update.emit(i)
            #注意，运行完统计操作之后需要等待几秒关闭线程之后再次点击 统计才会从头开始统计；
            # 点的太早会因为线程没有关闭导致下面这行代码还没运行，进而造成弹窗警告。
            self.ongoing = False
            # self.progressBar.setStyleSheet("QProgressBar::chunk { background-color: green; }")  # 设置进度条颜色为淡蓝色

        if self.ongoing:
            QMessageBox.warning(self.window,'警告','任务进行中，请等待完成')
            return

        worker = Thread(target=workerThreadFunc)
        worker.start()

    # 处理进度的slot函数
    def setProgress(self,value):
        self.progressBar.setValue(value)

app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()

"""
通过信号，在线程之间传递信息，对界面的操作都在主线程中完成。

"""