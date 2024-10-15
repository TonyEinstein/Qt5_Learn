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

# 2.常见的样式属性

### 2.1背景
可以指定某些元素的背景色，像这样

`QTextEdit { background-color: yellow }`

颜色可以使用红绿蓝数字，像这样

`QTextEdit { background-color: #e7d8d8 }`

也可以像这样指定背景图片

`QTextEdit {   background-image: url(gg03.png); `

### 2.2边框
可以像这样指定边框  `border:1px solid #1d649c;`
其中`1px`  是边框宽度， `solid`  是边框线为实线，  `dashed`(虚线) 和 `dotted`（点）

比如



```
*[myclass=bar2btn]:hover{
    border:1px solid #1d649c;
}
```

边框可以指定为无边框 border:none

### 2.3字体、大小、颜色

可以这样指定元素的 文字字体、大小、颜色

`*{ font-family:微软雅黑; font-size:15px; color: #1d649c;}`

### 2.4宽度、高度

可以这样指定元素的 宽度、高度

`QPushButton {  width:50px; height:20px;}`

### margin、padding

见下图，理解margin、padding 的概念：

![image](https://cdn2.byhy.net/imgs/api/20200405184322_921970.png)

可以这样指定元素的 元素的 margin

`QTextEdit {  margin:10px 11px 12px 13px}`

分别指定了元素的上右下左margin。 也可以使用 margin-top, margin-right, margin-bottom, margin-left 单独指定 元素的上右下左margin
比如


```
QTextEdit {
margin:10px 50px;  
padding:10px 50px;}
```
