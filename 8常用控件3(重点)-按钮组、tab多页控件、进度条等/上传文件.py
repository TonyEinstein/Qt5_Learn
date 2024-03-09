#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/4 16:37
# file: 上传文件.py
# author: chenruhai
# email: ruhai.chen@qq.com

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QFileDialog
import pandas as pd

class FileViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Excel File Viewer")
        self.setGeometry(100, 100, 600, 400)

        self.button = QPushButton("Select File", self)
        self.button.setGeometry(50, 50, 100, 30)
        self.button.clicked.connect(self.open_file)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(50, 100, 500, 250)

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xlsx)", options=options)

        if file_name:
            df = pd.read_excel(file_name)
            self.text_edit.setPlainText(df.to_string())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileViewer()
    window.show()
    sys.exit(app.exec_())
