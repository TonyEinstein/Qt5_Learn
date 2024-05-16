import time
from PySide2.QtCore import QThreadPool, QRunnable, Signal, QObject, Slot
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTextEdit, QTabWidget, QWidget

class WorkerSignals(QObject):
    # 代表含义是获取结果的信号，这里的Signal括号是返回去的变量的类型。str代表的是result这个信号的信号值是字符串内容。
    # 即self.signals.result.emit("信号值")的括号里面必须是字符串，这个字符串被返回到主线程让主线程接收使用。
    result = Signal(str)
    # 代表含义是线程结束的信号，没有信号值就只是作为标识使用。主线程会接收到没有值的信号值，这个时候对应的槽函数就不应该有参数。
    finished = Signal()

class Worker(QRunnable):
    def __init__(self, start, end ,tab_id):
        super().__init__()
        self.start = start
        self.end = end
        self.tab_id = tab_id
        self.signals = WorkerSignals()

    def run(self):
        for i in range(self.start, self.end):
            result = i * i * i
            # 下面是WorkerSignals()实例调用了result信号，emit函数是发出信号值。然后在主线程里面接收信号即可。
            self.signals.result.emit(f"{i} * {i} = {result}")
            time.sleep(0.1)
        # 全部计算完成后，调用完成信号通知主线程。
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
        # 本来是点击了才开始实例化并创建线程，但已经在主线程实例化线程池，在这里无需再进行实例化线程池
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
        # 本来是点击了才开始实例化并创建线程，但已经在主线程实例化线程池，在这里无需再进行实例化线程池
        # self.thread_pool = QThreadPool()
        self.worker = Worker(0, 20,self.tab_id)
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
