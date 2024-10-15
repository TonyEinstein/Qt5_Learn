#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 下午5:08
# file: 2.2数据处理进度案例.py
# author: chenruhai
# email: ruhai.chen@qq.com
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QProgressBar
from PySide2.QtCore import QThread, Signal
import time

class DataProcessor(QThread):
    progress_update = Signal(int)

    def run(self):
        for i in range(101):
            self.progress_update.emit(i)
            time.sleep(0.1)

class DataProcessingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.progress_bar = QProgressBar()
        self.start_button = QPushButton("Start Data Processing")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.start_button)
        self.setLayout(self.layout)

        self.processor = DataProcessor()
        self.processor.progress_update.connect(self.update_progress)

        self.start_button.clicked.connect(self.start_processing)

        self.setWindowTitle("Data Processing App")
        self.show()

    def start_processing(self):
        self.processor.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    data_processing_app = DataProcessingApp()
    sys.exit(app.exec_())