#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/6 10显示样式-选择器、属性、设置css等【未完】:51
# file: 菜单工具状态.py
# author: chenruhai
# email: ruhai.chen@qq.com

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from ui.demoOneUI import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow): #继承QMainWindow类和自己ui文件转化的py 类文件
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self) #加载ui 布局

        self.actionOpen.triggered.connect(self.openClick) # 绑定 actionOpen 按钮的trigger动作到openClick函数
        self.actionClose.triggered.connect(self.closeClick)
        self.actionsave.triggered.connect(self.saveClick)

        self.actionToolOpenFile.triggered.connect(self.openClick) #将自定义的具栏的 actionToolOpenFile 点击事件绑定到 openClick函数
        self.actionToolSaveFile.triggered.connect(self.saveClick)

        self.beautifulWords()  #美化文字
        self.setLabLink() #设定 链接文字
        self.labSetBaddy() #设定 lab 快捷绑定
        self.addStateBarView() #添加状态栏提示

    def openClick(self):
        print("click open")

    def closeClick(self):
        print("close click")

    def saveClick(self):
        print("save click")

    #美化文字颜色和字体
    def beautifulWords(self):
        self.label_text.setStyleSheet("QLabel{color:rgb(225,22,173,255);font-size:30px;font-family:Arial;"
                                   "background-color:gold;}")
    #设置lab 超链接
    def setLabLink(self):
        self.labe_link.setText("<A href='www.baidu.com'>百度</a>") #设置含超链接文本
       #允许 labe_link 控件访问超链接,默认不允许访问超链接，需要使用 setOpenExternalLinks(True) 允许
        self.labe_link.setOpenExternalLinks(True)
        self.labe_link.linkHovered.connect(self.slipLab) #监听鼠标停放滑过在超链接的事件

 # 鼠标停放超链接 lab 信号触发
    def slipLab(self):
        print("S鼠标停放滑过超链接属性的 lab")

  #绑定组件快捷方式
    def labSetBaddy(self):
        self.label_name.setBuddy(self.lineEdit_Name)
        self.label_Age.setBuddy(self.lineEdit_Age)

#设置状态栏显示
    def addStateBarView(self):
        self.labState = QLabel()
        self.labState.setText("State: busy")
        self.labTime = QLabel()
        self.labTime.setText("时间：11:00")

        self.statusBar.addPermanentWidget(self.labState,stretch=3)
        self.statusBar.addPermanentWidget(self.labTime, stretch=1)


if __name__ == '__main__':      #函数入口程序
    app = QApplication(sys.argv) #创建了一个QApplication对象，对象名为app
    win = MainWindow()  # 实体化类
    win.show() #显示
    sys.exit(app.exec_())

