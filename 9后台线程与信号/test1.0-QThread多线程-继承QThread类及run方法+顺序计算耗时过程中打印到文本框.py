import sys
import time
import concurrent.futures
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QTabWidget
from PySide2.QtCore import QObject, Signal, Slot, QThread

# !/usr/bin python3
# -*- encoding=utf-8 -*-
# Description :
# Author  :
# @Email :
# @File : 01_thread.py
# @Time : 2023-06-27 15:37:08
# @Project : qt

from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QWidget, QApplication, QPushButton


class Work(QThread):
    result = Signal()

    def __init__(self):
        QThread.__init__(self)

    def run(self) -> None:
        for i in range(0, 10):
            print('i = {}'.format(i))
            self.usleep(1000000)
        self.result.emit()


class Widget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self._work = Work()
        self._work.result.connect(self._result)
        self._widget()

    def _widget(self):
        _btn = QPushButton('确定')
        _btn.setParent(self)
        _btn.clicked.connect(self._run)

    def _run(self):
        self._work.start()

    def _result(self):
        print('线程结束')


if __name__ == '__main__':
    app = QApplication()

    window = Widget()
    window.show()

    app.exec_()

"""
1、优点：可以通过信号槽与外界进行通信。
2、缺点：
1）每次新建一个线程都需要继承QThread，实现一个新类，使用不太方便。
2）要自己进行资源管理，线程释放和删除。并且频繁的创建和释放会带来比较大的内存开销。
3、适用场景：QThread适用于那些常驻内存的任务。

"""