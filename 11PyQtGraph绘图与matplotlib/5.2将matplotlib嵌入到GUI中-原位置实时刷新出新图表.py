#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 上午10:36
# file: 5.2将matplotlib嵌入到GUI中-原位置实时刷新出新图表.py
# author: chenruhai
# email: ruhai.chen@qq.com

import sys
import random
import matplotlib.pyplot as plt
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide2.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MatplotlibWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title('Random Data Plot')
        self.ax.set_xlabel('X Axis')
        self.ax.set_ylabel('Y Axis')

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # 每隔1秒更新一次数据

        self.hover_line = self.ax.axhline(color='gray', linewidth=0.8, linestyle='--')
        self.text_annotation = self.ax.text(0.5, 0.9, '', transform=self.ax.transAxes, ha='center')
        self.canvas.mpl_connect('motion_notify_event', self.on_hover)

    def update_plot(self):
        x = list(range(10))
        y = [random.randint(0, 10) for _ in range(10)]

        self.ax.clear()
        # self.ax.plot(x, y)
        # self.canvas.draw()
        line, = self.ax.plot(x, y, color='blue')
        self.ax.set_title('Random Data Plot')
        self.ax.set_xlabel('X Axis')
        self.ax.set_ylabel('Y Axis')
        self.canvas.draw_idle()

    def on_hover(self, event):
        if event.inaxes == self.ax:
            x, y = event.xdata, event.ydata
            self.hover_line.set_ydata(y)
            self.text_annotation.set_text(f'X: {x:.2f}, Y: {y:.2f}')
            self.canvas.draw_idle()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matplotlib in PySide2")
        self.setGeometry(100, 100, 800, 600)

        central_widget = MatplotlibWidget()
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())