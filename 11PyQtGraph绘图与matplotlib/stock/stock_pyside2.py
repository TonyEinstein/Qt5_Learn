from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import pyqtgraph as pg

class Stock:

    def __init__(self):

        loader = QUiLoader()

        # pyside2 一定要 使用registerCustomWidget
        # 来 注册 ui文件中的第三方控件，
        loader.registerCustomWidget(pg.PlotWidget)
        self.ui = loader.load("main.ui")

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # 通过控件名称 historyPlot，找到Qt designer设计的 控件
        self.ui.historyPlot.plot(hour,temperature)


app = QApplication([])
stock = Stock()
stock.ui.show()
app.exec_()