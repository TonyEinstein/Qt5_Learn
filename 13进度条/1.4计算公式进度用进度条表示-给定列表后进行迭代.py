#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 下午3:44
# file: 1.4计算公式进度用进度条表示-给定列表后进行迭代.py
# author: chenruhai
# email: ruhai.chen@qq.com
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton, QVBoxLayout, QWidget, QTextBrowser
from PySide2.QtCore import QBasicTimer, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 设置窗口标题和大小
        self.setWindowTitle('列表20次方计算进度条示例')
        self.setGeometry(100, 100, 500, 400)

        # 创建要计算的列表
        self.values_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 90, 91, 92, 93, 94,
                            95, 96, 97, 98, 99, 100]
        self.list_length = len(self.values_list)  # 列表长度

        # 创建进度条组件
        self.progress_bar = QProgressBar(self)
        # 设置进度条的最小值为0，最大值为列表的长度
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(self.list_length)

        # 创建文本浏览器，用于显示每次计算的结果
        self.text_browser = QTextBrowser(self)

        # 创建按钮组件
        self.start_button = QPushButton('开始计算', self)
        self.start_button.clicked.connect(self.start_calculation)

        self.pause_button = QPushButton('暂停计算', self)
        self.pause_button.clicked.connect(self.pause_calculation)

        self.continue_button = QPushButton('继续计算', self)
        self.continue_button.clicked.connect(self.continue_calculation)

        self.reset_button = QPushButton('重置', self)
        self.reset_button.clicked.connect(self.reset_calculation)

        # 布局设置，将组件垂直排列
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.text_browser)
        layout.addWidget(self.start_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.continue_button)
        layout.addWidget(self.reset_button)

        # 设置中央窗口部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 初始化计时器
        self.timer = QBasicTimer()
        self.current_index = 0  # 当前计算的位置索引
        self.is_paused = False  # 暂停标志

    # 开始计算的函数
    def start_calculation(self):
        if not self.timer.isActive():  # 如果计时器未启动
            self.timer.start(100, self)  # 启动计时器，间隔100ms，触发timerEvent
            self.start_button.setEnabled(False)  # 禁用开始按钮防止重复点击

    # 暂停计算
    def pause_calculation(self):
        self.is_paused = True  # 将暂停标志设为True

    # 继续计算
    def continue_calculation(self):
        if self.is_paused:
            self.is_paused = False  # 恢复计算
            self.timer.start(100, self)  # 重新启动计时器

    # 重置计算
    def reset_calculation(self):
        self.timer.stop()  # 停止计时器
        self.current_index = 0  # 重置当前索引
        self.progress_bar.setValue(0)  # 重置进度条
        self.text_browser.clear()  # 清空文本框
        self.start_button.setEnabled(True)  # 启用开始按钮
        self.is_paused = False  # 重置暂停标志

    # 定时器事件，每次定时器触发时计算一次次方
    def timerEvent(self, event):
        if self.is_paused:  # 如果处于暂停状态，什么也不做
            return

        if self.current_index < self.list_length:  # 判断是否已经计算完所有的值
            value = self.values_list[self.current_index]  # 获取当前值
            result = value ** 20  # 计算当前值的20次方
            self.text_browser.append(f"{value}^20 = {result}")  # 输出结果到文本框
            self.progress_bar.setValue(self.current_index + 1)  # 更新进度条
            self.current_index += 1  # 移动到下一个索引
        else:
            self.timer.stop()  # 如果计算完毕，停止计时器
            self.start_button.setEnabled(True)  # 允许重新开始


# 启动应用程序
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
