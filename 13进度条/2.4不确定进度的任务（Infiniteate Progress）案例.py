#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 下午5:18
# file: 2.4不确定进度的任务（Infiniteate Progress）案例.py
# author: chenruhai
# email: ruhai.chen@qq.com
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QProgressBar, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Indeterminate Progress Bar")

        # 创建进度条（不确定状态）
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)  # 设置为不确定状态

        # 创建按钮
        self.button = QPushButton("Start Task")
        self.button.clicked.connect(self.start_task)

        # 创建布局
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.button)

        # 设置中央窗口部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_task(self):
        print("已经点击开始")
        # 模拟一个不确定进度的任务
        self.progress_bar.setRange(0, 0)  # 设置为不确定状态

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



"""
有时，我们不知道任务的具体细节，比如当下载文件大小未知时，可以使用不确定状态的细节条。
通过设置QProgressBar的范围为(0, 0)，可以显示不确定细节的状态（类似无限循环的细节条）。
"""