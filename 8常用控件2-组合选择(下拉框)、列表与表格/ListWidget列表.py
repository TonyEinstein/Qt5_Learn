#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/6 15:55
# file: ComboBox组合选择框.py
# author: chenruhai
# email: ruhai.chen@qq.com
import time

from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义,从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了,比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/列表ui.ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('列表组件示例')
        """
         1.添加一个列表项到列表末尾
         如果你要添加的列表项并非简单的文本，而是，比如有图标、则需要添加参数是一个 QListWidgetItem 。
        """
        self.ui.listWidget.addItem("366号")
        # 创建QListWidgetItem实例
        listItem = QListWidgetItem()
        # 设置图标
        listItem.setIcon(QIcon("ui/图标.ico"))
        # 可以给该列表项关联任意的对象，也可以不关联。
        # listItem.deviceCtrl = deviceCtrl
        # 添加到列表控件中
        self.ui.listWidget.addItem(listItem)
        """
        2. 添加多个列表项
        可以使用 addItems 方法来添加多个列表项到 末尾，参数是包含了多个列表项文本的列表
        """
        self.ui.listWidget.addItems(['396', '386', '376'])

        # 3.插入项到某一行
        self.ui.listWidget.insertItem(0, "Item Text")

        # 3.获取某个item是第几行【这里有bug，一直获得值都是-1】
        print("获取的item项是第\t{}\t行：".format(self.ui.listWidget.row(QListWidgetItem().setText("364"))))

        # 3.删除一个列表项；可以使用 takeItem 方法来删除1个列表项，参数是该列表项所在行.这里是第几个项是从0索引开始算起的。
        self.ui.listWidget.takeItem(1)

        # 4.清空列表项;可以使用 clear 方法来清空列表项，也就是删除选择框内所有的列表项
        # self.ui.listWidget_3.clear()

        """
        # 5.设置某个列表项为当前列表项;可以通过 setCurrentItem 方法，设置某个列表项为当前列表项
        # 【就是把某个列表项设置为listWidget_3变量的当前值】
        """
        self.ui.listWidget_3.addItems(['396', '386', '376'])
        self.ui.listWidget_3.setCurrentItem(QListWidgetItem().setText("386"))
        # 6.获取当前列表项文本；currentItem 方法可以得到列表当前选中项对象（QListWidgetItem） ，再调用这个对象的 text 方法，就可以获取文本内容【第一种方法bug报错】
        # print(self.ui.listWidget_3.currentItem().text())
        print(self.ui.listWidget_3.item(0).text())

        # 7.遍历列表项；
        for i in range(self.ui.listWidget_2.count()):
            # 取出列表项
            listItem = self.ui.listWidget_2.item(i)
            print(listItem.text())

        # 8.信号：选项选择改变；如果用户鼠标或者键盘选择了一个选项，Qt就会发出 itemSelectionChanged 信号，可以这样指定处理该信号的函数。
        self.ui.listWidget.itemSelectionChanged.connect(self.handleSelectionChange)

        # 9.信号：选项文本改变;如果列表项文本可以编辑，并且用户修改了文本，Qt就会发出 itemChanged 信号，可以这样指定处理该信号的函数【bug来着，因为根本无法改变】
        self.ui.listWidget_2.itemChanged.connect(self.handleItemTextChange)


    # 设备列表项选择改变 信号处理
    def handleSelectionChange(self):
        # 当前选择项目
        currentItem = self.ui.listWidget.currentItem().text()
        print("正在点击或选中：\t",currentItem)

    # 设备列表项选择改变 信号处理;参数 item 是修改的   QListWidgetItem对象
    def handleItemTextChange(self, item):
        print(item)



app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()