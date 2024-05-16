import sys
import time

from PySide2.QtCore import QThreadPool, QRunnable, Signal, QObject, Slot
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTextEdit, QTabWidget, QWidget


class WorkerSignals(QObject):
    # 代表含义是获取结果的信号，这里的Signal括号是返回去的变量的类型。str代表的是result这个信号的信号值是字符串内容。
    # 即self.signals.result.emit("信号值")的括号里面必须是字符串，这个字符串被返回到主线程让主线程接收使用。
    result = Signal(str)
    # 代表含义是线程结束的信号，没有信号值就只是作为标识使用。主线程会接收到没有值的信号值，这个时候对应的槽函数就不应该有参数。
    finished = Signal()

"""
请注意，使用QThread的时候，Signal()的实例化是直接放在Worker()里面的。
现在使用QThreadPool的情况下，Signal()的实例化单独写在一个类里面。当然也可以直接实例化，写在一个类里面是封装、方便调用。
"""

class Worker(QRunnable):
    def __init__(self, start, end ,tab_id):
        super().__init__()
        self.start = start
        self.end = end
        self.tab_id = tab_id
        self.signals = WorkerSignals()

    def run(self):
        """
        耗时计算任务
        :return:
        """
        for i in range(self.start, self.end):
            result = i * i * i
            # 下面是WorkerSignals()实例调用了result信号，emit函数是发出信号值。然后在主线程里面接收信号即可。
            self.signals.result.emit(f"{i} * {i} = {result}")
            time.sleep(0.1)
        # 全部计算完成后，调用完成信号通知主线程。
        self.signals.finished.emit()

class Tab1(QWidget):
    def __init__(self,tab_id):
        super().__init__()
        self.initUI()
        self.tab_id = tab_id

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.button = QPushButton("开始计算", self)
        self.text_edit = QTextEdit(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text_edit)
        # 点击之后执行该函数
        self.button.clicked.connect(self.start_calculation)

    def start_calculation(self):
        # 点击了才开始实例化并创建线程
        self.thread_pool = QThreadPool()
        # 下面的代码是实例化一个worker，自动就运行了run()方法里面的运算了。
        self.worker = Worker(0, 100,self.tab_id)
        # 这里为该耗时操作开启一个线程
        self.thread_pool.start(self.worker)
        # 下面的代码是开启线程中的信号和主线程信号的连接传输
        self.worker.signals.result.connect(self.update_text)
        # 完成计算后的退出提示
        self.worker.signals.finished.connect(self.task_finished)

    @Slot()
    def update_text(self, text):
        self.text_edit.append(text)

    @Slot()
    def task_finished(self):
        # 无需手动释放资源，QThreadPool启动线程执行完成后会自动释放。
        print("{}线程结束".format(self.tab_id))

class Tab2(QWidget):
    # Tab2的实现与Tab1类似，只需修改start_calculation方法中的参数即可
    def __init__(self,tab_id):
        super().__init__()
        self.initUI()
        self.tab_id = tab_id

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.button = QPushButton("开始计算", self)
        self.text_edit = QTextEdit(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text_edit)
        self.button.clicked.connect(self.start_calculation)

    def start_calculation(self):
        # 点击了才开始实例化并创建线程
        self.thread_pool = QThreadPool()
        self.worker = Worker(0, 1000,self.tab_id)
        # 这里真正开启一个线程
        self.thread_pool.start(self.worker)
        # 下面的代码是开启线程中的信号和主线程信号的连接传输
        self.worker.signals.result.connect(self.update_text)
        # 完成计算后的退出提示
        self.worker.signals.finished.connect(self.task_finished)

    @Slot()
    def update_text(self, text):
        self.text_edit.append(text)

    @Slot()
    def task_finished(self):
        # 无需手动释放资源，QThreadPool启动线程执行完成后会自动释放。
        print("{}线程结束".format(self.tab_id))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tab_widget = QTabWidget(self)
        self.setGeometry(100, 100, 800, 600)
        self.setCentralWidget(self.tab_widget)
        self.tab1 = Tab1(1)
        self.tab2 = Tab2(2)
        self.tab_widget.addTab(self.tab1, "Tab1")
        self.tab_widget.addTab(self.tab2, "Tab2")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
