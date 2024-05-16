#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/5/15 下午5:06
# file: test1.1改进【推荐】-QThread多线程-继承QThread类及run方法+顺序计算耗时过程中打印到文本框.py
# author: chenruhai
# email: ruhai.chen@qq.com
import sys
import time

from PySide2.QtCore import Signal, QThread, Slot
from PySide2.QtWidgets import QWidget, QTextEdit, QPushButton, QVBoxLayout, QMainWindow, QApplication, QTabWidget


class Worker(QThread):
    """
    信号：
        update_signal 更新信号
        finished 完成信号
    """
    # 定义一个信号标识finished，含义是完成耗时计算任务之后需要进行的操作。一般是退出和关闭线程
    finished = Signal()
    # update_signal，含义是在进行该耗时计算的过程中对提示信息进行实时打印。【注意，这里不是执行耗时计算结束后才打印到主线程，而是在执行过程中实时的反馈】
    update_signal = Signal(str)

    def __init__(self, tab_id):
        super().__init__()
        # 只是一个ID标识，要不要都可以。要的话可以标识第几个页面
        self.tab_id = tab_id

    def run(self) -> None:
        for i in range(10):
            result = i * i * 3
            # .emit 是发送信号。发送do_work中的任务每次执行打印的信号,emit(str)的内容str就是发送到主线程的信号值。
            # update_signal是发送信号的标识，代表该条信号用于更新信息或者提示或者报错，总之是更新信息的作用。
            self.update_signal.emit(f"Result from Tab {self.tab_id}: {result}")
            time.sleep(1)
        # 发送do_work完成的信号，
        # finished 是发送信号的标识。
        self.finished.emit()

class Tab(QWidget):
    def __init__(self, tab_id):
        super().__init__()
        self.tab_id = tab_id
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        self.button = QPushButton(f"Start Task in Tab {self.tab_id}")
        """
        注意，按钮点击一次之后将会连接到start_task开启新线程
        """
        self.worker = Worker(self.tab_id)
        self.button.clicked.connect(self.start_task)
        self.layout.addWidget(self.button)

        # 将信号连接到槽函数，也就是将新创建的线程发送出来的信号用槽函数接收，
        # 槽函数中用text_edit实现接收打印，相当于给到了主线程的text_edit组件进行打印（text_edit.append）。
        self.worker.update_signal.connect(self.update_text)
        # 完成之后进行线程退出和关闭，避免资源浪费
        self.worker.finished.connect(self.task_finished)
    def start_task(self):
        # 开始一个新的线程，系统会自动分配一个新的线程给self.button.clicked.connect(self.start_task)要执行的内容。
        # 注意，这里是worker开启新线程。因为Worker已经继承了QThread类
        self.worker.start()
        print("{}线程开始".format(self.tab_id))

    """
    比起方式2，更推荐这种方式，因为这种方式没有把text的内容进行固定模板，可发挥性大。
    """
    @Slot(str)
    def update_text(self, text):
        # 槽函数：接收新创建的线程发送过来的信号text，然后用append方法更新到GUI主线程的text_edit组件中
        self.text_edit.append(text)

    @Slot()
    def task_finished(self):
        # 槽函数：完成运算之后，该槽函数将刚才创建的线程销毁
        self.worker.quit()
        self.worker.wait()
        print("{}线程结束".format(self.tab_id))

class Tab2(QWidget):
    def __init__(self, tab_id):
        super().__init__()
        self.tab_id = tab_id
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.text_edit2 = QTextEdit()
        self.layout.addWidget(self.text_edit2)

        self.worker = Worker(self.tab_id)
        self.button2 = QPushButton(f"Start Task in Tab {self.tab_id}")
        self.button2.clicked.connect(self.start_task)
        self.layout.addWidget(self.button2)
        self.worker.update_signal.connect(self.update_text)
        self.worker.finished.connect(self.task_finished)
    def start_task(self):
        self.worker.start()
        print("{}线程开始".format(self.tab_id))

    @Slot(str)
    def update_text(self, text):
        self.text_edit2.append(text)

    @Slot()
    def task_finished(self):
        self.worker.quit()
        self.worker.wait()
        print("{}线程结束".format(self.tab_id))

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-processing Example")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        # QThread进行创建新线程的方式，无需在主类中此进行显式声明创建线程。只需要在各自页面类中进行创建即可额。
        # 所以这里是直接调用者两个页面，以保证页面中的按钮等功能可用。除了耗时计算要分配新线程防止堵塞界面(主线程)外，
        # 其它操作比如点击、滑动、浏览、查看、放大缩小等操作都是在主线程的。
        self.tab1 = Tab(1)
        self.tab_widget.addTab(self.tab1, "Tab 1")
        self.tab2 = Tab2(2)
        self.tab_widget.addTab(self.tab2, "Tab 2")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
