

**PySide2多线程问题示例：创建新线程、子线程发射信号到主界面**  
文章链接：https://blog.csdn.net/xhzc7/article/details/116702475
【为避免文章消失所以下载来放在这里了】

本文是在pyside学习过程中的记录，从无子线程、子线程在主程序中直接操作Qt界面、子线程发射信号操作主界面三个步骤出发，记录对多线程的一种处理方式。作为一名小白，若有描述不合理之处还请大神指出。  
以下主要包含两部分：  
1、问题展示  
2、代码展示

一、示例问题（随便整了一个简单的）：创建一个小程序，在一个界面输入最大最小值，在另一个界面依次打印出以下信息：从最小值开始，每次加1，到最大值后结束。  
先给出三个方式的结果：  
1、只有一个主程序：在操作界面填入信息，点击开始按钮后，无法再点击界面上其他任何东西，多次点击后程序卡住，直到打印完毕后才反应过来![只有一个主程序](https://img-blog.csdnimg.cn/20210512121740709.gif#pic_center)  
2、添加新线程，但是新线程直接操作主界面，程序执行时，再操作主界面，直接崩溃。。。。。。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210512122515843.gif#pic_center)  
3、还是让子线程发射信号给一个函数，然后间接操作主界面吧，终于好了！！！能够在打印数字的同时对界面进行其他操作！  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210512122840414.gif#pic_center)  
二、上述三种方式的代码，都传了一遍，好做对比，ui文件是用Qt设计师做的，因为界面很简单就不上传了  
1、只有一个主程序

```python
from PySide2.QtWidgets import QApplication,QWidget,QPlainTextEdit,QProgressBar
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from time import sleep

class Start1(QWidget):
    def __init__(self):
        #-----动态加载ui文件-------#
        qtmp = QFile("duoxiancheng.ui")# 导入Qt designer生成的界面ui文件
        qtmp.open(QFile.ReadOnly)
        qtmp.close()
        self.ui = QUiLoader().load(qtmp)

        self.ui.pushButton.clicked.connect(self.printFunc)  # 将pushButton按钮链接到打印函数

    #-------定义打印函数-----------#
    def printFunc(self):

        #-----读取输入的最大最小值--------#
        num_min = int(self.ui.lineEdit_min.text())
        num_max = int(self.ui.lineEdit_max.text())
        num = num_max - num_min + 1

        #---------打印函数的执行主体------------#
        for i in range(num):
            self.ui.plainTextEdit.appendPlainText(str(num_min))     # 输出到文本框
            self.ui.progressBar.setValue(int((i + 1) / num * 100))   # 给进度条赋值
            num_min += 1
            sleep(0.1)            # 休眠0.1秒，模拟实际运行时程序的耗时

if __name__ == '__main__':
    app = QApplication([])
    stats1 = Start1()
    stats1.ui.show()
    app.exec_()
```

2、增加新线程，利用thread类，创建新的线程

```python
from PySide2.QtWidgets import QApplication,QWidget,QPlainTextEdit,QProgressBar
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from threading import Thread  # 导入thread
from time import sleep

class Start1(QWidget):
    def __init__(self):
        #-----动态加载ui文件-------#
        qtmp = QFile("duoxiancheng.ui")
        qtmp.open(QFile.ReadOnly)
        qtmp.close()
        self.ui = QUiLoader().load(qtmp)

        self.ui.pushButton.clicked.connect(self.new_printFunc)  # 将pushButton按钮链接到新线程函数

    #-------定义打印函数-----------#
    def printFunc(self):

        #-----读取输入的最大最小值--------#
        num_min = int(self.ui.lineEdit_min.text())
        num_max = int(self.ui.lineEdit_max.text())
        num = num_max - num_min + 1

        #---------打印函数的执行主体------------#
        for i in range(num):
            self.ui.plainTextEdit.appendPlainText(str(num_min))     # 输出到文本框
            self.ui.progressBar.setValue(int((i + 1) / num * 100))   # 给进度条赋值
            num_min += 1
            sleep(0.1)            # 休眠0.1秒，模拟实际运行时程序的耗时

    #-------创建新线程函数------#
    def new_printFunc(self):
        thread = Thread(target=self.printFunc)  #此处省略了参数args=('参数1', '参数2')，仅指定了新线程入口函数（即我们定义好的打印函数）
        thread.start() # 开启新线程

if __name__ == '__main__':
    app = QApplication([])
    stats1 = Start1()
    stats1.ui.show()
    app.exec_()
```

3、通过信号函数操作主界面，这一步主要思想是将子线程中的值（在本例中是文本框中的数字和进度条的值）通过一个信号发送到主程序中，由主程序操作主界面。

```python
from PySide2.QtWidgets import QApplication,QWidget,QPlainTextEdit,QProgressBar
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from threading import Thread
from PySide2.QtCore import Signal,QObject  # 导入信号类
from time import sleep

class MySignals(QObject):
    # 定义一种信号，因为有文本框和进度条两个类，此处要四个参数，类型分别是： QPlainTextEdit 、 QProgressBar、字符串和整形数字
    # 调用 emit方法发信号时，传入参数必须是这里指定的参数类型
    # 此处也可分开写两个函数，一个是文本框输出的，一个是给进度条赋值的
    text_print = Signal(QPlainTextEdit,QProgressBar,str,int)
 

class Start1(QWidget):
    def __init__(self):
        #-----动态加载ui文件-------#
        qtmp = QFile("duoxiancheng.ui")
        qtmp.open(QFile.ReadOnly)
        qtmp.close()
        self.ui = QUiLoader().load(qtmp)

        self.ui.pushButton.clicked.connect(self.new_printFunc)

        self.ms = MySignals()                              #引入信号函数
        self.ms.text_print.connect(self.pF)           #将信号传递给主程序中pF函数进行处理

    def new_printFunc(self): # 新线程入口函数
        thread = Thread(target=self.printFunc)
        thread.start()

    def printFunc(self):    #打印函数
        num_min=int(self.ui.lineEdit_min.text())
        num_max=int(self.ui.lineEdit_max.text())
        num=num_max-num_min+1
        for i in range(num):
            #此处不再直接操作主界面，而是发射信号给MySignals函数中的text_print，
            #传递参数包括要操作哪个位置和要操作的内容
            self.ms.text_print.emit(self.ui.plainTextEdit,self.ui.progressBar,str(num_min),int((i+1)/num*100))  
            num_min+=1
            sleep(0.1)

    #接收到发来的信号，pt和pb就是要操作的位置self.ui.plainTextEdit和self.ui.progressBar，text和int1则是具体内容
    def pF(self,pt,pb,text,int1):
        pt.appendPlainText(text)
        pb.setValue(int1)

if __name__ == '__main__':
    app = QApplication([])
    stats1 = Start1()
    stats1.ui.show()
    app.exec_()

```
