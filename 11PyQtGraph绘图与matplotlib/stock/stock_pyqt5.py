from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, uic

class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # PyQt5 直接加载ui文件
        # 因为 第三方控件通过promote的定义
        # 已经可以知道 控件类所在模块的路径
        self.ui = uic.loadUi("main.ui")

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        self.ui.historyPlot.plot(hour, temperature)

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()