#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 上午11:47
# file: 2.2显示多张图片.py
# author: chenruhai
# email: ruhai.chen@qq.com
import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class MultiImageViewer(QGraphicsView):
    def __init__(self, image_paths):
        super(MultiImageViewer, self).__init__()

        scene = QGraphicsScene()
        self.setScene(scene)

        for index, image_path in enumerate(image_paths):
            pixmap = QPixmap(image_path)
            item = QGraphicsPixmapItem(pixmap)
            item.setPos(0, index * pixmap.height())  # 设置图片在视图中的位置
            scene.addItem(item)

        # 调整视图的大小以适应所有图片
        scene.setSceneRect(scene.itemsBoundingRect())
        self.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    image_paths = ["../图标/01/png 128 49/blockdevice.png",
                   "../图标/01/png 128 49/blockdevice.png",
                   "../图标/01/png 128 49/blockdevice.png"]
    viewer = MultiImageViewer(image_paths)
    viewer.show()

    sys.exit(app.exec_())