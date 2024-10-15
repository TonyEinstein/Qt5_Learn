#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 上午9:10
# file: 3.2j将PyQtGraph图表作为控件嵌入ui文件中.py
# author: chenruhai
# email: ruhai.chen@qq.com
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import pyqtgraph as pg

class Stock:

    def __init__(self):

        loader = QUiLoader()

        # pyside2 一定要 使用registerCustomWidget
        # 来注册 ui文件中的第三方控件，这样加载的时候
        # loader才知道第三方控件对应的类，才能实例化对象
        loader.registerCustomWidget(pg.PlotWidget)
        self.ui = loader.load("stock/main.ui")

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # 通过控件名称 historyPlot，找到Qt designer设计的 控件
        self.ui.historyPlot.plot(hour,temperature)

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