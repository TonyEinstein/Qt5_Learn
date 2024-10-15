#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 下午3:26
# file: 1.2进度条入门实现.py
# author: chenruhai
# email: ruhai.chen@qq.com
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton, QVBoxLayout, QWidget
from PySide2.QtCore import QBasicTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 创建进度条
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(30, 40, 200, 25)  # 设置位置和大小
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)

        # 创建一个按钮
        self.button = QPushButton('开始', self)
        self.button.setGeometry(30, 80, 200, 40)
        self.button.clicked.connect(self.start_progress)

        # 创建计时器
        self.timer = QBasicTimer()
        self.step = 0  # 记录进度

        # 设置主窗口的布局
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_progress(self):
        # 如果计时器未启动则启动
        if self.timer.isActive() == False:
            self.timer.start(100, self)
            self.button.setText('停止')
        else:
            self.timer.stop()
            self.button.setText('开始')

    def timerEvent(self, event):
        # 更新进度条
        if self.step >= 100:
            self.timer.stop()
            self.button.setText('完成')
            return

        self.step += 1
        self.progress_bar.setValue(self.step)

# 应用程序的启动
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('进度条示例')
    window.resize(280, 170)
    window.show()
    sys.exit(app.exec_())
