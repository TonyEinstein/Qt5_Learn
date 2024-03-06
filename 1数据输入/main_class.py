#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main_class.py
# @Time      :2022/5/16 14:41
# @Author    : https://github.com/chenruhai?tab=repositories


from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox

class Stats():
    def __init__(self):
        # QMainWindow、QPlainTextEdit、QPushButton 是3个控件类，分别对应界面的主窗口、文本框、按钮;
        # 要在界面上 创建一个控件 ，就需要在程序代码中 创建 这个 控件对应类 的一个 实例对象。
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 300)
        self.window.setWindowTitle('薪资统计')

        """
        在 Qt 系统中，控件（widget）是 层层嵌套 的，除了最顶层的控件，其他的控件都有父控件。
        QPlainTextEdit、QPushButton 实例化时，都有一个参数window,就是指定它的父控件对象 是 window 对应的QMainWindow 主窗口。
        而 实例化 QMainWindow 主窗口时，却没有指定 父控件， 因为它就是最上层的控件了。
        """
        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入薪资表")
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('统计', self.window)
        self.button.move(380, 80)
        # 这个按钮被点击之后连接了这个handleCalc函数，执行了该handleCalc事件。
        self.button.clicked.connect(self.handleCalc)

    """
    在 Qt 系统中， 当界面上一个控件被操作时，比如 被点击、被输入文本、被鼠标拖拽等， 就会发出 信号 ，英文叫 signal 。就是表明一个事件（比如被点击、被输入文本）发生了。
    下面就是一个事件。
    """
    def handleCalc(self):
        print("-------------" * 2, "按钮被点击了,handleCalc事件被执行", "-------------" * 2)
        info = self.textEdit.toPlainText()
        print(info)
        print("-------------" * 2, "-------------" * 2)
        # 薪资20000 以上 和 以下 的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            # 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            name,salary,age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.window,
                    '统计结果',
                    f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                    )

if __name__ == '__main__':
    """
    QApplication 提供了整个图形界面程序的底层管理功能，比如：初始化、程序入口参数的处理，用户事件（对界面的点击、输入、拖拽）分发给各个对应的控件，等等…
    既然QApplication要做如此重要的初始化操作，所以，必须在任何界面控件对象创建前，先创建它。
    """
    app = QApplication([])

    stats = Stats()
    stats.window.show()
    # 进入QApplication的事件处理循环，接收用户的输入事件（），并且分配给相应的对象去处理。
    app.exec_()