#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 上午10:36
# file: 5.2将matplotlib嵌入到GUI中-原位置实时刷新出新图表.py
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

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def draw_plot(self):
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        self.ax.clear()
        self.ax.plot(x, y)
        self.canvas.draw()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matplotlib in PySide2 Example")
        self.resize(800, 600)

        self.matplotlib_widget = MatplotlibWidget()

        button = QPushButton("Draw Plot")
        button.clicked.connect(self.matplotlib_widget.draw_plot)

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