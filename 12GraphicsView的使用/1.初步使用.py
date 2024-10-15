#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/10/15 上午11:42
# file: 1.初步使用.py
# author: chenruhai
# email: ruhai.chen@qq.com
from PySide2.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsEllipseItem
from PySide2.QtCore import QRectF
from PySide2.QtGui import QBrush, QColor

import sys

# 创建一个简单的应用程序
app = QApplication(sys.argv)

# 创建 QGraphicsScene 对象，作为图形项的容器
scene = QGraphicsScene()

# 创建一个矩形图形项，并设置其位置和大小
rect_item = QGraphicsRectItem(QRectF(0, 0, 100, 100))
rect_item.setBrush(QBrush(QColor(255, 0, 0)))  # 设置矩形填充颜色为红色
scene.addItem(rect_item)  # 将矩形图形项添加到场景中

# 创建一个椭圆（圆）图形项，并设置其位置和大小
ellipse_item = QGraphicsEllipseItem(QRectF(150, 0, 100, 100))
ellipse_item.setBrush(QBrush(QColor(0, 255, 0)))  # 设置椭圆填充颜色为绿色
scene.addItem(ellipse_item)  # 将椭圆图形项添加到场景中

# 创建一个 QGraphicsView 对象，用于显示场景内容
view = QGraphicsView(scene)
view.setWindowTitle("GraphicsView 示例")
view.setGeometry(100, 100, 400, 300)  # 设置窗口位置和大小
# 启用鼠标拖拽
view.setDragMode(QGraphicsView.ScrollHandDrag)

# 缩放视图 (放大 2 倍)
# view.scale(2, 2)

# 显示 QGraphicsView
view.show()

# 启动应用程序事件循环
sys.exit(app.exec_())
