#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 上午11:29
# file: 5.5将matplotlib嵌入UI-绘制多个图表-独立的图表.py
# author: chenruhai
# email: ruhai.chen@qq.com
import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MatplotlibWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.figure1, self.ax1 = plt.subplots()
        self.canvas1 = FigureCanvas(self.figure1)

        self.figure2, self.ax2 = plt.subplots()
        self.canvas2 = FigureCanvas(self.figure2)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas1)
        layout.addWidget(self.canvas2)

        self.setLayout(layout)

    def draw_plots(self):
        x = np.linspace(0, 10, 100)
        y1 = np.sin(x)
        y2 = np.cos(x)

        self.ax1.clear()
        self.ax1.plot(x, y1)
        self.canvas1.draw()

        self.ax2.clear()
        self.ax2.plot(x, y2)
        self.canvas2.draw()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matplotlib in PySide2 Example")
        self.resize(800, 600)

        self.matplotlib_widget = MatplotlibWidget()

        button = QPushButton("Draw Plots")
        button.clicked.connect(self.matplotlib_widget.draw_plots)

        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(button)
        central_layout.addWidget(self.matplotlib_widget)
        central_widget.setLayout(central_layout)

        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())