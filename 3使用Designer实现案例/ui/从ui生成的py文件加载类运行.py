#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :从ui生成的py文件加载类运行.py
# @Time      :2022/5/18 16:20
# @Author    : https://github.com/chenruhai?tab=repositories


from PySide2.QtWidgets import QApplication,QMainWindow
from httpclient import Ui_HttpClient

# 注意 这里选择的父类 要和你UI文件窗体一样的类型
# 主窗口是 QMainWindow， 表单是 QWidget， 对话框是 QDialog
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_HttpClient()


        # 初始化界面
        self.ui.setupUi(self)

        # 使用界面定义的控件，也是从ui里面访问（这里一直莫名错误）
        self.ui.webview.load('http://www.baidu.com')

"""
这种方式会报错
"""

app = QApplication([])
mainw = MainWindow()
mainw.show()
app.exec_()
