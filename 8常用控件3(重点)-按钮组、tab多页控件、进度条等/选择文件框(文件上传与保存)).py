#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/3/7 9:04
# file: 获取日期.py
# author: chenruhai
# email: ruhai.chen@qq.com
import time

import pandas as pd
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QFileDialog


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义,从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了,比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/选择文件框(文件上传与保存).ui')
        self.setBaseSize(self.size())
        # self.setFixedSize(1000, 900)
        self.ui.setWindowTitle('选择文件框(文件上传)示例')
        """
        1.上传单个文件
        如果你想弹出文件选择框，选择一个 已经存在 的文件，可以使用 QFileDialog 静态方法 getOpenFileName。
        """
        self.ui.pushButton_2.clicked.connect(self.open_onefile)
        """
        2.保存单个文件
        想弹出文件选择框，选择路径和文件名，来 保存一个文件 ，可以使用 QFileDialog 静态方法 getSaveFileName
        """
        data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [30, 35, 40],
            'City': ['New York', 'San Francisco', 'Los Angeles']
        }
        self.df = pd.DataFrame(data)
        self.ui.pushButton_5.clicked.connect(self.save_onefile)

        """
        3.选择多个文件【可以是选择多个文件进行上传操作】
        如果要选择多个文件，使用 getOpenFileNames 静态方法;
        filePaths 对应的返回值是一个列表，里面包含了选择的文件。如果用户点击了 选择框的 取消选择按钮，返回 空列表。
        """
        self.ui.pushButton_3.clicked.connect(self.select_files)

        """
        4.选择目录【也可以进行选定目录之后保存文件】
        通过 getExistingDirectory 静态方法 选择目录。
        该方法，第一个参数是父窗口对象，第二个参数是选择框显示的标题。
        返回值即为选择的路径字符串。如果用户点击了 选择框的 取消选择按钮，返回 空字符串。
        """
        self.ui.pushButton_4.clicked.connect(self.select_dir)

    def select_dir(self):
        """
        返回值是一个列表，里面包含了选择的文件；还返回了过滤信息。
        如果用户点击了 选择框的 取消选择按钮，返回 空列表。
        :return:
        """
        dirPath = QFileDialog.getExistingDirectory(
            self.ui,  # 父窗口对象
            "选择存储路径",  # 标题
            r"./ui",  # 起始目录
        )
        print("已选择的文件夹：\t",dirPath)

    def select_files(self):
        """
        返回值是一个列表，里面包含了选择的文件；还返回了过滤信息。
        如果用户点击了 选择框的 取消选择按钮，返回 空列表。
        :return:
        """
        filePaths, filetypes = QFileDialog.getOpenFileNames(
            self.ui,  # 父窗口对象
            "选择你要上传的文件",  # 标题
            r"./ui",  # 起始目录
            "图片类型 (*.png *.jpeg *.bmp *.jpg)"  # 选择类型过滤项，过滤内容在括号中
        )
        print("已选择的文件：\t",filePaths,"\t过滤信息是：",filetypes)

    def save_onefile(self):
        """
        该方法返回值 是一个元组，第一个元素是选择的文件路径，第二个元素是文件类型，如果你只想获取文件路径即可，可以采用上面的代码写法。
        如果用户点击了 选择框的 取消选择按钮，返回 空字符串。
        :return:
        """
        filePath, filetype = QFileDialog.getSaveFileName(
            self.ui,  # 父窗口对象
            "保存文件：",  # 标题
            r"./ui",  # 起始目录
            "Excel类型 (*.xlsx)"  # 选择类型过滤项，过滤内容在括号中，只有不过滤的才会显示出来。
        )

        if filePath:
            # 保存文件操作
            self.df.to_excel(filePath,encoding="utf-8",index=False)
        print("已保存的文件：\t",filePath,"\t",filetype)


    # 这个文件和上面的选择单个文件一样
    def open_onefile(self):
        """
        该方法返回值 是一个元组，第一个元素是选择的文件路径，第二个元素是文件类型，如果你只想获取文件路径即可，可以采用上面的代码写法。
        如果用户点击了 选择框的 取消选择按钮，返回 空字符串。
        :return:
        """
        filePath, filetype = QFileDialog.getOpenFileName(
            self.ui,  # 父窗口对象
            "选择你要上传的文件",  # 标题
            r"./ui",  # 起始目录
            "图片类型 (*.png *.jpeg *.bmp *.jpg)"  # 选择类型过滤项，过滤内容在括号中
        )
        print("已选择的文件：\t",filePath,"\t",filetype)



app = QApplication([])
window = MyWindow()
window.ui.show()
app.exec_()