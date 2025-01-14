#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/7 16:20
# file: 树控件1入门.py
# author: chenruhai
# email: ruhai.chen@qq.com


from PySide2.QtWidgets import QApplication, QHeaderView
from PySide2.QtUiTools import QUiLoader

# 导入 QTreeWidget, QTreeWidgetItem, QIcon
from PySide2.QtWidgets import  QTreeWidget, QTreeWidgetItem
from PySide2.QtGui import QIcon

class SomeWindow:

    def __init__(self):

        self.ui = QUiLoader().load('ui/树控件QTreeWidgetItem.ui')
        self.ui.setGeometry(100, 100, 800, 600)
        # 调用设置树控件
        self.setupTree()

    def setupTree(self):
        # 获取树控件对象
        tree = self.ui.tree

        # 1.是否隐藏标头栏
        tree.setHeaderHidden(False)
        header = tree.header()
        # 2.让列宽度 自适应 内容【自适应宽度之后，启动界面后将不可更改】
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        # 获取树控件的不可见根节点
        root = tree.invisibleRootItem()

        # 准备一个folder节点
        folderItem = QTreeWidgetItem()
        # 创建图标对象
        folderIcon = QIcon("ui/folder.png")
        # 设置节点图标
        folderItem.setIcon(0, folderIcon)
        # 设置该节点  第1个column 文本
        folderItem.setText(0, '学员李辉')
        # 添加到树的不可见根节点下，就成为第一层节点
        root.addChild(folderItem)
        # 设置该节点为展开状态
        folderItem.setExpanded(True)

        # 准备一个 叶子 节点
        leafItem = QTreeWidgetItem()
        # leafIcon = QIcon("./Images/leaf.gif")
        # 设置节点图标
        # leafItem.setIcon(0, leafIcon)
        # 设置该节点  第1个column 文本
        leafItem.setText(0, '作业 - web自动化1')
        # 设置该节点  第2个column 文本
        leafItem.setText(1, '提交日期20200101')
        # 添加到 叶子节点 到 folerItem 目录节点下
        folderItem.addChild(leafItem)




app = QApplication([])
w = SomeWindow()
w.ui.show()
app.exec_()

"""
注意：

每个 节点 都是 QTreeWidgetItem 对象;添加节点 必须通过 该节点的 父节点;可以使用 addChild 方法，添加到最后;
也可以使用 insertChild 方法，插入到指定位置，比如folderItem.insertChild(2, leafItem)就插入到 第3个 子节点的位置上，因为第1个子节点的索引是0。
如果控件宽度不够，字符串会显示为省略号。
"""