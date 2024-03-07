from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from threading import Thread


class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/main.ui')
        self.ui.setWindowTitle('海运数据爬取分析')

        #代码去设置QSS

        # 1.设置主窗口直接是白色的。【相当于对MainWindow进行设置QSS，那么其下的子组件都将用这个QSS】
        # self.ui.setAttribute(Qt.WA_StyledBackground, True)
        # self.ui.setStyleSheet("background-color: white")

        #2.设置组件
        self.ui.crawl.setStyleSheet("QPushButton {"
                         "  background-color: rgb(255, 0, 0);"  # 红色
                         "  color: rgb(255, 255, 255);"         # 白色文本
                         "}")

"""
Qt有种定义界面显示样式的方法，称之为 Qt Style Sheet ，简称 QSS，它的 语法和用途 和 CSS 特别的相似。

如果在设计师界面上 最上层的 MainWindow 对象 styleSheet 属性指定如下的内容：
QPushButton { 
    color: red ;
    font-size:15px;
}

就会发现，所有的按钮上的文字都变成了红色的，并且字体变大了。
注意这个指定界面元素 显示样式的 语法，由 selector 和 declaration 组成。
花括号前面的 部分，比如示例中的 QPushButton 称之为 selector。
花括号后面的 部分，称之为 Properties （样式属性）
"""

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()