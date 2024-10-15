#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 上午9:58
# file: 4.1轴刻度转为字符串值.py
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
        # self.plotItem.getViewBox().setBackgroundColor((12GraphicsView的使用, 249, 238)) # 设置图表背景色


        # 创建定时器，每隔一段时间更新绘图数据
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # 每隔1秒更新一次数据

    def update_plot(self):
        # 生成随机数据
        self.hour.append(len(self.hour) + 1)
        self.temperature.append(random.randint(10, 40))
        # 更新绘图,将点绘制到图表上并且绘制线条
        self.plot.setData(self.hour, self.temperature)

        # 将x轴的整数刻度转成字符串形式（假设用"第n小时"作为例子）
        x_ticks = [(i, f"第{i}小时") for i in self.hour]
        self.plotItem.getAxis('bottom').setTicks([x_ticks])


app = QApplication([])
stock = Stock()
stock.ui.show()
app.exec_()