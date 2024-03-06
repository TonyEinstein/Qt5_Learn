#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main_order.py
# @Time      :2022/5/16 14:25
# @Author    : https://github.com/chenruhai?tab=repositories

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox

"""
QApplication 提供了整个图形界面程序的底层管理功能，比如：初始化、程序入口参数的处理，用户事件（对界面的点击、输入、拖拽）分发给各个对应的控件，等等…
既然QApplication要做如此重要的初始化操作，所以，必须在任何界面控件对象创建前，先创建它。
"""
app = QApplication([])

"""
在 Qt 系统中， 当界面上一个控件被操作时，比如 被点击、被输入文本、被鼠标拖拽等， 就会发出 信号 ，英文叫 signal 。就是表明一个事件（比如被点击、被输入文本）发生了。
下面就是一个事件。
"""
def handleCalc():
    print("-------------"*2,"按钮被点击了,handleCalc事件被执行","-------------"*2)
    info = textEdit.toPlainText()
    print(info)
    print("-------------"*2,"-------------"*2)
    # 薪资20000 以上 和 以下 的人员名单
    salary_above_20k = ''
    salary_below_20k = ''
    for line in info.splitlines():
        if not line.strip():
            continue
        parts = line.split(' ')
        # 去掉列表中的空字符串内容,获取每一行的内容
        parts = [p for p in parts if p]
        print(parts)
        name,salary,age = parts
        if int(salary) >= 20000:
            salary_above_20k += name + '\n'
        else:
            salary_below_20k += name + '\n'

    QMessageBox.about(window,
                '统计结果',
                f'''薪资20000 以上的有：\n{salary_above_20k}
                \n薪资20000 以下的有：\n{salary_below_20k}'''
                )


# QMainWindow、QPlainTextEdit、QPushButton 是3个控件类，分别对应界面的主窗口、文本框、按钮;
# 要在界面上 创建一个控件 ，就需要在程序代码中 创建 这个 控件对应类 的一个 实例对象。
window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('薪资统计')

"""
在 Qt 系统中，控件（widget）是 层层嵌套 的，除了最顶层的控件，其他的控件都有父控件。
QPlainTextEdit、QPushButton 实例化时，都有一个参数window,就是指定它的父控件对象 是 window 对应的QMainWindow 主窗口。
而 实例化 QMainWindow 主窗口时，却没有指定 父控件， 因为它就是最上层的控件了。
"""
textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10,25)
textEdit.resize(300,350)

button = QPushButton('统计', window)
button.move(380,80)
# 这个按钮被点击之后连接了这个handleCalc函数，执行了该handleCalc事件。
button.clicked.connect(handleCalc)


window.show()

# 进入QApplication的事件处理循环，接收用户的输入事件（），并且分配给相应的对象去处理。
app.exec_()


#
# if __name__ == "__main__":
#     run_code = 0
"""
薛蟠     4560 25
薛蝌     4460 25
薛宝钗   35776 23
薛宝琴   14346 18
王夫人   43360 45
王熙凤   24460 25
王子腾   55660 45
王仁     15034 65
尤二姐   5324 24
贾芹     5663 25
贾兰     13443 35
贾芸     4522 25
尤三姐   5905 22
贾珍     54603 35

"""