#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/6 13:40
# file: PlainTextEdit多行纯文本框.py
# author: chenruhai
# email: ruhai.chen@qq.com
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义,从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了,比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/多行纯文本框ui.ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('多行纯文本框操作')
        """
        1.信号：文本被修改（无参数返回）
        当文本框中的内容被键盘编辑，被点击就会发出 textChanged 信号，可以这样指定处理该信号的函数;
        注意： Qt在调用这个信号处理函数时，不会传入文本框目前的内容字符串，作为参数,这个行为 和 单行文本框不同。
        """
        self.ui.plainTextEdit.textChanged.connect(self.handleTextChange)
        """
        2.信号：光标位置改变
        当文本框中的光标位置变动，就会发出 cursorPositionChanged 信号，可以这样指定处理该信号的函数
        """
        self.ui.plainTextEdit_2.cursorPositionChanged.connect(self.handleChanged)
        # 3.获取文本，通过 toPlainText 方法获取编辑框内的文本内容。
        text = self.ui.plainTextEdit_3.toPlainText()
        print(text)

        #4.获取选中文本获取 QTextCursor 对象
        textCursor = self.ui.plainTextEdit_4.textCursor()
        selection = textCursor.selectedText()
        print("选中的文本是：\n",selection)

        # 5.设置提示：通过 setPlaceholderText 方法可以设置提示文本内容
        self.ui.plainTextEdit_5.setPlaceholderText('文本提示内容')

        # 6.设置文本：通过 setPlainText 方法设置编辑框内的文本内容 为参数里面的文本字符串
        self.ui.plainTextEdit_6.setPlainText('''你好，乔布斯
        hello 雷布斯''')

        # 7.在末尾添加文本;通过 appendPlainText 方法在编辑框末尾添加文本内容;注意：这种方法会在添加文本后 自动换行.
        self.ui.plainTextEdit_7.appendPlainText('你好，九键')

        # 8.在光标处插入文本；通过 insertPlainText 方法在编辑框首部添加文本内容；注意：这种方法 不会 在添加文本后自动换行
        self.ui.plainTextEdit_8.insertPlainText('你好，海上生明月')

        # 9.清除所有文本，clear 方法可以清除编辑框内所有的文本内容
        self.ui.plainTextEdit_9.clear()

        # 12GraphicsView的使用 设置最大行数，有时候，代码会不断往文本框添加内容，为了防止占用过多资源，可以设置文本框最大行数。
        self.ui.plainTextEdit_12.document().setMaximumBlockCount(3)

    def handleChanged(self):
        print("光标位置在改变，包括编辑位置和新增内容都是在改变哦")


    def handleTextChange(self):
        print("多行纯文本框 文本被修改，这里不会有返回值作为信号函数的参数；每编辑一次会执行一次该函数")


"""
注意：在苹果MacOS上，有 更新文本框内容后，需要鼠标滑过才能更新显示的bug，参考这里(https://bugreports.qt.io/browse/PYSIDE-871)
文本浏览框 内置了一个 QTextDocument 类型的对象 ，存放文档。
"""


app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()
