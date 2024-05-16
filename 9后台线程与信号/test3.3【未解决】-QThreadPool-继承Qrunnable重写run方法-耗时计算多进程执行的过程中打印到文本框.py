import concurrent.futures
import time
from multiprocessing import Queue

from PySide2.QtCore import QThreadPool, QRunnable, Signal, QObject, Slot, QMetaObject, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTextEdit, QTabWidget, QWidget


def calculate(args):
    i, signals  = args
    result = i * i * i
    signals.result.emit(f"{i} * {i} = {result}")
    time.sleep(0.5)
    print("i:{}".format(i))
    return result
class WorkerSignals(QObject):
    # 代表含义是获取结果的信号，这里的Signal括号是返回去的变量的类型。str代表的是result这个信号的信号值是字符串内容。
    # 即self.signals.result.emit("信号值")的括号里面必须是字符串，这个字符串被返回到主线程让主线程接收使用。
    result = Signal(str)
    # 代表含义是线程结束的信号，没有信号值就只是作为标识使用。主线程会接收到没有值的信号值，这个时候对应的槽函数就不应该有参数。
    finished = Signal()

class Worker(QRunnable):
    def __init__(self, start, end,tab_id):
        super().__init__()
        self.start = start
        self.end = end
        self.tab_id = tab_id
        self.signals = WorkerSignals()

    def run(self):
        print("{}线程启动".format(self.tab_id))
        args = [(i, self.signals) for i in range(self.start, self.end)]
        with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
            results = executor.map(calculate,args)
            # 上面的results结果出来之后，就代表已经完成多进程计算了。
        self.signals.finished.emit()
class Tab1(QWidget):
    def __init__(self,thread_pool,tab_id):
        super().__init__()
        self.thread_pool = thread_pool
        self.tab_id = tab_id
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.button = QPushButton("开始计算", self)
        self.text_edit = QTextEdit(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text_edit)
        self.button.clicked.connect(self.start_calculation)

    def start_calculation(self):
        # self.thread_pool = QThreadPool()
        self.worker = Worker(0, 10,self.tab_id)
        self.worker.signals.result.connect(self.update_text)
        self.thread_pool.start(self.worker)
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
    def __init__(self, thread_pool,tab_id):
        super().__init__()
        self.thread_pool = thread_pool
        self.tab_id = tab_id
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.button = QPushButton("开始计算", self)
        self.text_edit = QTextEdit(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text_edit)
        self.button.clicked.connect(self.start_calculation)

    def start_calculation(self):
        # self.thread_pool = QThreadPool()
        self.worker = Worker(0, 30,self.tab_id)
        self.worker.signals.result.connect(self.update_text)
        self.thread_pool.start(self.worker)
        # 完成计算后的退出提示
        self.worker.signals.finished.connect(self.task_finished)

    @Slot()
    def update_text(self, text):
        # self.text_edit.append(text)
        QMetaObject.invokeMethod(self.text_edit, "append", Qt.QueuedConnection, [text])

    @Slot()
    def task_finished(self):
        # 无需手动释放资源，QThreadPool启动线程执行完成后会自动释放。
        print("{}线程结束".format(self.tab_id))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.thread_pool = QThreadPool.globalInstance()
        self.initUI()

    def initUI(self):
        self.tab_widget = QTabWidget(self)
        self.setGeometry(100, 100, 800, 600)
        self.setCentralWidget(self.tab_widget)
        self.tab1 = Tab1(self.thread_pool,1)
        self.tab2 = Tab2(self.thread_pool,2)
        self.tab_widget.addTab(self.tab1, "Tab1")
        self.tab_widget.addTab(self.tab2, "Tab2")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
