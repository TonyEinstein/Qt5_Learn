#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 上午9:10
# file: 3.2j将PyQtGraph图表作为控件嵌入ui文件中.py
# author: chenruhai
# email: ruhai.chen@qq.com

from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QTimer
import pyqtgraph as pg
import random

class Stock:
    def __init__(self):
        self.loader = QUiLoader()

        # pyside2 一定要 使用registerCustomWidget
        # 来注册 ui文件中的第三方控件，这样加载的时候
        # loader才知道第三方控件对应的类，才能实例化对象
        self.loader.registerCustomWidget(pg.PlotWidget)
        self.ui = self.loader.load("stock/main.ui")

        self.hour = []
        self.temperature = []
        # 设置整个图表的背景色
        self.ui.historyPlot.setBackground((240, 240, 240))
        # 通过控件名称 historyPlot，找到Qt designer设计的 控件
        # self.plot = self.ui.historyPlot.plot(self.hour, self.temperature)

        # 通过控件名称 historyPlot，找到Qt designer设计的 控件
        self.plot = self.ui.historyPlot.plot(self.hour, self.temperature, pen=(255, 0, 0))  # 设置线条颜色为红色
        self.plotItem = self.ui.historyPlot.getPlotItem()
        self.plotItem.setTitle("Temperature History")  # 设置标题
        self.plotItem.titleLabel.setText('Temperature History', color=(0, 0, 0))  # 设置标题字体颜色为黑色
        self.plotItem.setLabel('left', 'Temperature', units='C')  # 设置y轴名称和单位
        self.plotItem.setLabel('bottom', 'Time', units='h')  # 设置x轴名称和单位
        self.plotItem.showGrid(x=True, y=True)  # 显示网格线
        self.plotItem.getAxis('bottom').setPen((12, 4, 2))  # 设置x轴颜色
        self.plotItem.getAxis('left').setPen((12, 4, 2))  # 设置y轴颜色
        # self.plotItem.getViewBox().setBackgroundColor((240, 240, 240)) # 设置图表背景色

        # 创建定时器，每隔一段时间更新绘图数据
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # 每隔1秒更新一次数据

    def update_plot(self):
        # 生成随机数据
        self.hour.append(len(self.hour) + 1)
        self.temperature.append(random.randint(10, 40))

        # 仅显示绘制保留最近的10个数据点
        # if len(self.hour) > 10:
        #     self.hour = self.hour[-10:]
        #     self.temperature = self.temperature[-10:]

        # 更新绘图,将点绘制到图表上并且绘制线条
        self.plot.setData(self.hour, self.temperature)

app = QApplication([])
stock = Stock()
stock.ui.show()
app.exec_()


"""
1.PyQtGraph图形可以作为一个 Qt的 widget控件，嵌入到 Qt 程序主窗口中。可以在 Qt Designer 中把 PyQtGraph图形控件 作为第三方控件 加入。

2.通过 Qt Designer，我们可以预先把界面上的控件的位置大小设计好，然后动态加载把数据加载进去即可。


3.但是 界面上摆放的都是 Qt内置的控件， 那么像 PyQtGraph 里面的 PlotWidget这种第三方控件怎么 放到 Qt Designer中呢？【最重要】
    在UI设计中，界面是没有PlotWidget这个控件的，需要先随意加一个Label或者文本框、widget，然后右键 选择“提升为”中选择 PlotWidget，这样控件才会变成 PlotWidget控件。
     具体做法：通过 Qt Designer 放一个 第三方控件 的 上层layout， 然后在代码中 创建 第三方控件对象（文本框或者label都可以、或者widget）， 并且添加到 上层layout 里面去。
"""