#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 上午11:31
# file: test.py
# author: chenruhai
# email: ruhai.chen@qq.com
import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MatplotlibWidget(QWidget):
    def __init__(self, output_widget):
        super().__init__()

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.output_widget = output_widget

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.output_widget)

        self.setLayout(layout)

    def draw_plot(self):
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        self.ax.clear()
        self.ax.plot(x, y)
        self.canvas.draw()

        self.output_widget.append("Matplotlib plot drawn.")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matplotlib in PySide2 Example")
        self.resize(800, 600)

        self.output_widget = QTextEdit()
        self.matplotlib_widget = MatplotlibWidget(self.output_widget)

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