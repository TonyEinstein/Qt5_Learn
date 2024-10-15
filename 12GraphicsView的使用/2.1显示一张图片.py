#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 上午11:45
# file: 2.1显示一张图片.py
# author: chenruhai
# email: ruhai.chen@qq.com
import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class ImageViewer(QGraphicsView):
    def __init__(self, image_path):
        super(ImageViewer, self).__init__()

        scene = QGraphicsScene()
        self.setScene(scene)

        pixmap = QPixmap(image_path)
        item = QGraphicsPixmapItem(pixmap)
        scene.addItem(item)

        self.fitInView(item, Qt.KeepAspectRatio)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    image_path = "../图标/01/png 128 49/blockdevice.png"
    viewer = ImageViewer(image_path)
    viewer.show()

    sys.exit(app.exec_())