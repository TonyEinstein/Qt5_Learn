#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 上午9:07
# file: 3.1实时更新图.py
# author: chenruhai
# email: ruhai.chen@qq.com
from PySide2 import QtWidgets
from pyqtgraph.Qt import  QtCore
import pyqtgraph as pg
import sys
from random import randint

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('pyqtgraph作图')

        # 创建 PlotWidget 对象
        self.pw = pg.PlotWidget()

        # 设置图表标题
        self.pw.setTitle("气温趋势",
                         color='#008080',
                         size='12pt')

        # 设置上下左右的label
        self.pw.setLabel("left","气温(摄氏度)")
        self.pw.setLabel("bottom","时间")

        # 设置Y轴 刻度 范围
        self.pw.setYRange(min=-10, # 最小值
                          max=50)  # 最大值

        # 显示表格线
        self.pw.showGrid(x=True, y=True)

        # 背景色改为白色
        self.pw.setBackground('w')

        # 设置Y轴 刻度 范围
        self.pw.setYRange(min=-10, # 最小值
                          max=50)  # 最大值

        # 居中显示 PlotWidget
        self.setCentralWidget(self.pw)

        # 实时显示应该获取 PlotDataItem对象, 调用其setData方法，
        # 这样只重新plot该曲线，性能更高
        self.curve = self.pw.plot(
            pen=pg.mkPen('r', width=1)
        )

        self.i = 0
        self.x = [] # x轴的值
        self.y = [] # y轴的值

        # 启动定时器，每隔1秒通知刷新一次数据
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateData)
        self.timer.start(1000)

    def updateData(self):
        self.i += 1
        self.x.append(self.i)
        # 创建随机温度值
        self.y.append(randint(10,30))

        # plot data: x, y values
        self.curve.setData(self.x,self.y)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = MainWindow()
    main.show()
    app.exec_()

"""
要画动态的实时更新图，只需要在把变更的内容重新plot即可。
"""

"""
1.PyQtGraph图形可以作为一个 Qt的 widget控件，嵌入到 Qt 程序主窗口中。可以在 Qt Designer 中把 PyQtGraph图形控件 作为第三方控件 加入。

2.通过 Qt Designer，我们可以预先把界面上的控件的位置大小设计好，然后动态加载把数据加载进去即可。


3.但是 界面上摆放的都是 Qt内置的控件， 那么像 PyQtGraph 里面的 PlotWidget这种第三方控件怎么 放到 Qt Designer中呢？【最重要】
    在UI设计中，界面是没有PlotWidget这个控件的，需要先随意加一个Label或者文本框、widget，然后右键 选择“提升为”中选择 PlotWidget，这样控件才会变成 PlotWidget控件。
     具体做法：通过 Qt Designer 放一个 第三方控件 的 上层layout， 然后在代码中 创建 第三方控件对象（文本框或者label都可以、或者widget）， 并且添加到 上层layout 里面去。
"""