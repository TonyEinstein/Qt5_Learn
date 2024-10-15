#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 下午5:07
# file: 2.1下载器案例.py
# author: chenruhai
# email: ruhai.chen@qq.com
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QProgressBar
from PySide2.QtCore import QThread, Signal
import time

class Downloader(QThread):
    progress_update = Signal(int)

    def run(self):
        """
        这里写工作代码，写下载的代码以及更新进度条
        :return:
        """
        # 下载列表:101个url下载对象
        for i in range(101):
            """
            在这发起网络请求并下载保存到本地，保存完成一次就更新一次信号
            """
            self.progress_update.emit(i)
            time.sleep(0.1)

class FileDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.progress_bar = QProgressBar()
        self.start_button = QPushButton("Start Download")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.start_button)
        self.setLayout(self.layout)

        self.downloader = Downloader()
        self.downloader.progress_update.connect(self.update_progress)

        self.start_button.clicked.connect(self.start_download)

        self.setWindowTitle("File Downloader")
        self.show()

    def start_download(self):
        self.downloader.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    downloader_app = FileDownloader()
    sys.exit(app.exec_())