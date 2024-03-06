#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/6 10:02
# file: stats_qt5实现.py
# author: chenruhai
# email: ruhai.chen@qq.com

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


class Stats:
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = uic.loadUi("ui/stats.ui")
        # self.ui = uic.loadUi("ui/stats.ui")
        # 点击该按钮的时候连接该函数
        self.ui.pushButton.clicked.connect(self.handleCalc)

    def handleCalc(self):
        # 获取该按钮输入的文字信息
        info = self.ui.Input.toPlainText()
        print(info)
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')

            parts = [p for p in parts if p]
            name,salary,age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        self.ui.Output.setPlaceholderText(f'''薪资20000 以上的有：\n{salary_above_20k}\n薪资20000 以下的有：\n{salary_below_20k}''')

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()

