#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/7 9:57
# file: 菜单栏和菜单.py
# author: chenruhai
# email: ruhai.chen@qq.com
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon

class Window(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()
        self.resize(600,200)

        # 1.创建 菜单栏QMenuBar 对象 并返回
        menuBar = self.menuBar()
        """
        菜单和action的区别，菜单点击之后是可以选择子菜单的；而actione是一个动作、相当当信号，点击后会执行某个操作。
        """
        # 2.一级菜单
        fileMenu = menuBar.addMenu("文件")
        editMenu = menuBar.addMenu("编辑")
        helpMenu = menuBar.addMenu("帮助")
        # 3.一级Action
        actionHomePage = menuBar.addAction('主页')
        actionHomePage.triggered.connect(self.actionHomePageClicked)
        """
        点击 菜单Action， 会触发信号 triggered， 处理点击菜单的的代码；
        self.ui.actionOpenFile.triggered.connect(self.openPageFile)
        """
        # 4.一级菜单的 action项
        actionAddNode = fileMenu.addAction(QIcon("./ui/图标.ico"),"添加")
        fileMenu.addSeparator() # 分隔符
        actionDelNode = fileMenu.addAction("删除")
        actionAddNode.triggered.connect(self.actionAddNodeClicked)
        actionDelNode.triggered.connect(self.actionDelNodeClicked)

        # 5.二级菜单
        edit_1 = editMenu.addMenu("插入图表")
        edit_2 = editMenu.addMenu("插入图片")

        # 6.二级菜单的 action项
        action1 = edit_1.addAction("action1")
        action2 = edit_1.addAction("action2")

        """
        也可以在 Qt Designer上很方便的为 QMainWindow 类型的窗口添加菜单。上面的操作都能在设计师里面完成。
        """

    def actionHomePageClicked(self):
        print('actionHomePageClicked')

    def actionAddNodeClicked(self):
        print('actionAddNodeClicked')

    def actionDelNodeClicked(self):
        print('actionDelNodeClicked')

"""
菜单里面还可以有子菜单，就是这样:
菜单栏（QMenuBar） ->  菜单（QMenu）->  子菜单（QMenu） -> QAction

注意：上面说的子菜单，并不是一种新的类型，也是 QMenu ， 只是从属于其他Qmenu， 就像 QLayout 形成的层级关系一样。
菜单里面 点击能触发操作的条目，称之为 QAction ，中文叫 动作
"""


app = QtWidgets.QApplication([])
ex = Window()
ex.show()
app.exec_()