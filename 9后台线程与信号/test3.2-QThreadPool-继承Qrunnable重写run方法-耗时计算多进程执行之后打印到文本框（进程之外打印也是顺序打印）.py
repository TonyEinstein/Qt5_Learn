import concurrent.futures
import time
from PySide2.QtCore import QThreadPool, QRunnable, Signal, QObject, Slot
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTextEdit, QTabWidget, QWidget


def calculate(i):
    result = i * i * i
    time.sleep(0.5)
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
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(calculate, range(self.start,self.end))
            # 上面的results结果出来之后，就代表已经完成多进程计算了。
            # 下面的打印信号都是在上面的耗时计算之外。
            for i, result in enumerate(results):
                self.signals.result.emit(f"Result from Tab {self.tab_id}: {result}")
            # 当然也可以定义一个信号将耗时计算完成之后的results结果值直接返回，也可以按照上面的一个一个内容的打印信号返回。
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
        self.text_edit.append(text)

    @Slot()
    def task_finished(self):
        # 无需手动释放资源，QThreadPool启动线程执行完成后会自动释放。
        print("{}线程结束".format(self.tab_id))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.thread_pool = QThreadPool()
        """
        QThreadPool.globalInstance() 是一个静态方法，用于获取全局共享的线程池实例。
        在 PySide2 中，QThreadPool 的全局实例可以通过这个方法获取，可以用于在整个应用程序中管理线程的执行。
        """
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
