#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 上午11:49
# file: 2.3轮番阅览某一目录下的图片-并显示信息.py
# author: chenruhai
# email: ruhai.chen@qq.com
import sys
import os
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class ImageViewer(QWidget):
    def __init__(self):
        super(ImageViewer, self).__init__()

        self.image_paths = self.load_image_paths("../图标/01/png 64 49/")
        self.current_index = 0

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)

        self.image_info_label = QLabel()

        self.load_image(self.current_index)

        self.prev_button = QPushButton("Previous")
        self.next_button = QPushButton("Next")

        self.prev_button.clicked.connect(self.show_previous_image)
        self.next_button.clicked.connect(self.show_next_image)

        image_layout = QVBoxLayout()
        image_layout.addWidget(self.view)
        image_layout.addWidget(self.image_info_label)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.next_button)

        layout = QVBoxLayout()
        layout.addLayout(image_layout)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def load_image_paths(self, directory):
        image_paths = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(('.jpg', '.png', '.jpeg'))]
        return image_paths

    def load_image(self, index):
        if 0 <= index < len(self.image_paths):
            pixmap = QPixmap(self.image_paths[index])
            item = QGraphicsPixmapItem(pixmap)
            self.scene.clear()
            self.scene.addItem(item)

            # 显示图片信息
            image_name = os.path.basename(self.image_paths[index])
            image_size = os.path.getsize(self.image_paths[index])
            image_info = f"Name: {image_name}\nSize: {image_size} bytes"
            self.image_info_label.setText(image_info)

    def show_previous_image(self):
        self.current_index = (self.current_index - 1) % len(self.image_paths)
        self.load_image(self.current_index)

    def show_next_image(self):
        self.current_index = (self.current_index + 1) % len(self.image_paths)
        self.load_image(self.current_index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())