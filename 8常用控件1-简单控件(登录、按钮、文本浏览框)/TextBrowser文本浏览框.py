#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/6 14:53
# file: TextBrowser文本浏览框.py
# author: chenruhai
# email: ruhai.chen@qq.com

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义,从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了,比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/文本浏览框ui.ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('文本浏览框示例')

        """
        1.在末尾添加文本：通过 append 方法在编辑框末尾添加文本内容。注意：这种方法会在添加文本后 自动换行。
        浏览框里面的内容长度超出了可见范围，我们在末尾添加了内容，往往希望控件自动翻滚到当前添加的这行，
        可以通过 ensureCursorVisible 方法来实现.
        """
        self.ui.textBrowser.append("你好，婆罗萨。")
        # self.ui.textBrowser.ensureCursorVisible()

        """
        2.通过 insertPlainText 方法在编辑框末尾添加文本内容，注意：这种方法 不会 在添加文本后自动换行。
        """
        self.ui.textBrowser_2.insertPlainText('你好，白月黑羽')


    def handleChanged(self):
        print("光标位置在改变，包括编辑位置和新增内容都是在改变哦")


    def handleTextChange(self):
        print("多行纯文本框 文本被修改，这里不会有返回值作为信号函数的参数；每编辑一次会执行一次该函数")



app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()



"""
QTextBrowser 是 只能查看文本 控件。
通常用来显示一些操作日志信息、或者不需要用户编辑的大段文本内容。
"""