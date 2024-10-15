
# 1.QSS与CSS
官方文档：https://doc.qt.io/qt-5/stylesheet-syntax.html

Qt有种定义界面显示样式的方法，称之为 Qt Style Sheet ，简称 QSS，它的 语法和用途 和 CSS 特别的相似。

如果在设计师界面上 最上层的 MainWindow 对象 styleSheet 属性指定如下的内容：

```
QPushButton {
    color: red ;
    font-size:15px;
}
```
就会发现，所有的按钮上的文字都变成了红色的，并且字体变大了。
注意这个指定界面元素 显示样式的 语法，由 selector 和 declaration 组成。
花括号前面的 部分，比如示例中的 QPushButton 称之为 selector。
花括号后面的 部分，称之为 Properties （样式属性）

---------------------

# 2写代码去设置QSS
前面的（1QSS选择器.md和2QSS常见的样式属性.md）示例都是在Qt设计师软件中设置样式。

也可以写代码直接设置样式， 比如，给控件设置背景色：
```
class QMyWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # 给控件设置背景色
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: white")
```

