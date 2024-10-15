#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 上午9:05
# file: 2.1柱状图.py
# author: chenruhai
# email: ruhai.chen@qq.com
from PySide2 import QtWidgets
import pyqtgraph as pg

class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('pyqtgraph作图示例')

        # 创建 PlotWidget 对象
        self.pw = pg.PlotWidget()
        # 设置图表标题
        self.pw.setTitle("订单数量",color='#008080',size='12pt')
        # 背景色改为白色
        self.pw.setBackground('w')
        # 设置上下左右的label
        self.pw.setLabel("left", "订单量(条)")
        self.pw.setLabel("bottom", "日期")

        # 显示表格线
        self.pw.showGrid(x=True, y=True)


        # 产生两种柱状图数据，分别对应 红色柱 和蓝色柱
        x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        y1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        x2 = [0.33, 1.33, 2.33, 3.33, 4.33, 5.33, 6.33, 7.33, 8.33, 9.33]
        y2 = [0.33, 1.33, 2.33, 3.33, 4.33, 5.33, 6.33, 7.33, 8.33, 9.33]

        bg1 = pg.BarGraphItem(x=x1, height=y1, width=0.3, brush='r')
        bg2 = pg.BarGraphItem(x=x2, height=y2, width=0.3, brush='g')

        # 添加到界面上
        self.pw.addItem(bg1)
        self.pw.addItem(bg2)


        # 创建其他Qt控件
        okButton = QtWidgets.QPushButton("OK")
        lineEdit = QtWidgets.QLineEdit('点击信息')
        # 水平layout里面放 edit 和 button
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(lineEdit)
        hbox.addWidget(okButton)

        # 垂直layout里面放 pyqtgraph图表控件 和 前面的水平layout
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.pw)
        vbox.addLayout(hbox)

        # 设置全局layout
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = MainWindow()
    main.show()
    app.exec_()