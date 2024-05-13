#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/5/10 下午6:43
# file: tes.py
# author: chenruhai
# email: ruhai.chen@qq.com
from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QVBoxLayout, QWidget

class MyComboBox(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ComboBox Example')

        layout = QVBoxLayout()

        self.comboBox = QComboBox()
        self.comboBox.addItem("Option 1")
        self.comboBox.addItem("Option 2")
        self.comboBox.addItem("Option 3")
        self.comboBox.currentTextChanged.connect(self.on_combo_box_changed)
        layout.addWidget(self.comboBox)
        # 将comboBox选择的结果实时赋值给label
        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def on_combo_box_changed(self, text):
        print(text)
        self.result_label.setText(f"Selected: {text}")

if __name__ == '__main__':
    app = QApplication([])
    window = MyComboBox()
    window.show()
    app.exec_()
