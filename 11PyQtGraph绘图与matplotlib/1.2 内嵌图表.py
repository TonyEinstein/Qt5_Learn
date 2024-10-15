#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 上午9:03
# file: 1.2 内嵌图表.py
# author: chenruhai
# email: ruhai.chen@qq.com

from PySide2 import QtWidgets
import pyqtgraph as pg

class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # 画图-------------------------------------------
        self.setWindowTitle('pyqtgraph作图示例')

        # 创建 PlotWidget 对象
        self.pw = pg.PlotWidget()

        # 设置图表标题
        self.pw.setTitle("气温趋势",color='#008080',size='12pt')

        # 设置上下左右的label
        self.pw.setLabel("left","气温(摄氏度)")
        self.pw.setLabel("bottom","时间")
        # 背景色改为白色
        self.pw.setBackground('w')


        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # hour 和 temperature 分别是 : x, y 轴上的值
        self.pw.plot(hour,
                     temperature,
                     pen=pg.mkPen('b') # 线条颜色
                    )

        # 创建其他Qt控件-----------------------------------
        okButton = QtWidgets.QPushButton("OK")
        lineEdit = QtWidgets.QLineEdit('点击信息')


        # 水平layout里面放 edit 和 button---------------------
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(lineEdit)
        hbox.addWidget(okButton)

        # 垂直layout里面放 pyqtgraph图表控件 和 前面的水平layout---------
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.pw)
        vbox.addLayout(hbox)

        # 设置全局layout----------
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = MainWindow()
    main.show()
    app.exec_()