
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
# 2.QSS的选择器selector
花括号前面的 部分称之为 selector（中文可以叫 选择器），用来 告诉Qt 哪些特征的元素 是你要设定显示效果的。
比如：QPushButton 选择所有类型为 QPushButton （包括其子类） 的界面元素 。
QSS selector语法 几乎 和 Web CSS 的 selector语法没有什么区别。

## selector常见语法

| Selector | 示例 | 说明 |
| --- | --- | --- |
| Universal Selector | `*` | 星号匹配所有的界面元素 |
| Type Selector | `QPushButton` | 选择所有 QPushButton类型 （包括其子类） |
| Class Selector | `.QPushButton` | 选择所有 QPushButton类型 ，但是不包括其子类 |
| ID Selector | `QPushButton#okButton` | 选择所有 `对象名为 okButton` 的QPushButton类型 |
| Property Selector | `QPushButton[flat="false"]` | 选择所有 flat 属性值为 false 的 QPushButton类型。 |
| Descendant Selector | `QDialog QPushButton` | 选择所有 QDialog `内部` QPushButton类型 |
| Child Selector | `QDialog > QPushButton` | 选择所有 QDialog `直接子节点` QPushButton类型 |

## Pseudo-States 伪状态

可以这样指定当鼠标移动到一个元素上方的时候，元素的显示样式

`QPushButton:hover { color: red }`

再比如，指定一个元素是disable状态的显示样式

`QPushButton:disabled { color: red }`

再比如，指定一个元素是鼠标悬浮，并且处于勾选（checked）状态的显示样式

`QCheckBox:hover:checked { color: white }`

## 优先级

如果一个元素的显示样式被多层指定了， `越靠近元素本身` 的选择指定，优先级越高


