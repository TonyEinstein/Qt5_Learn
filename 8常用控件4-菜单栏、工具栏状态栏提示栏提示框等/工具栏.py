#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/7 15:01
# file: 工具栏.py
# author: chenruhai
# email: ruhai.chen@qq.com
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon

class Window(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()
        self.resize(600,200)

        # 创建 工具栏 对象 并添加
        toolbar = QtWidgets.QToolBar(self)
        self.addToolBar(toolbar)

        # 添加 工具栏 条目Action
        actionAddNode = toolbar.addAction(QIcon("./Images/folder.png"),"添加")
        actionAddNode.triggered.connect(self.actionAddNodeClicked)
        """
        添加工具栏后，还要在工具栏上添加 条目Action （中文称之为： 动作 ）。方法是点击右下角 动作编辑器 ，新建动作。
        """
        action = toolbar.addAction("删除")
        action = toolbar.addAction("修改")
        action = toolbar.addAction("查询")
        toolbar.addSeparator()             # 添加分隔符
        action = toolbar.addAction("帮助")

    def actionAddNodeClicked(self):
        print('actionAddNodeClicked')

"""
工具里面的可以点击的条目 也是 QAction ，和菜单栏一样！
如果 菜单栏 和 工具栏有 相同的 action ，可以公用一个Action对象。
注意，只有 Main Window 类型的窗体，才能添加工具栏
"""

app = QtWidgets.QApplication([])
ex = Window()
ex.show()
app.exec_()