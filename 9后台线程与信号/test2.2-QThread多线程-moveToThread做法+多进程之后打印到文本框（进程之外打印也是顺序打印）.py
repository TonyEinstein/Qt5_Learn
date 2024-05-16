import sys
import time
import concurrent.futures
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QTabWidget
from PySide2.QtCore import QObject, Signal, Slot, QThread

def calculate(i):
    result = i * i
    time.sleep(1)
    return result

class Worker(QObject):
    finished = Signal()
    update_signal = Signal(str)

    def __init__(self, tab_id):
        super().__init__()
        self.tab_id = tab_id

    # ----------------------------------【1.concurrent.futures.ProcessPoolExecutor()实现进程池用于耗时计算】
    @Slot()
    def do_work(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(calculate, range(100))
            # 上面的results结果出来之后，就代表已经完成多进程计算了。
            # 下面的打印信号都是在上面的耗时计算之外。
            for i, result in enumerate(results):
                self.update_signal.emit(f"Result from Tab {self.tab_id}: {result}")
            # 当然也可以定义一个信号将耗时计算完成之后的results结果值直接返回，也可以按照上面的一个一个内容的打印信号返回。
        # 代表运行到此处的时候该线程才发出结束的信号
        self.finished.emit()
    #-------------------------------------------【2.with multiprocessing.Pool(max_workers=4) as pool实现多进程】
    # @Slot()
    # def do_work(self):
    #     with multiprocessing.Pool(max_workers=4) as pool:
    #         """
    #         executor.map()是ProcessPoolExecutor的一个方法，它接受一个函数和一个可迭代对象作为参数。它将函数应用于可迭代对象的每个元素。
    #         executor.map()是ProcessPoolExecutor的一个方法，它接受一个函数和一个可迭代对象作为参数。它将函数应用于可迭代对象的每个元素，并返回一个迭代器，该迭代器生成结果。
    #         """
    #         # 下面这段代码相当于 for i in range(10) : calculate(i, self.update_signal)
    #         results = pool.map(lambda i: calculate(i, self.update_signal), range(10))
    #         print("线程 {} 我被执行完毕了".format(self.tab_id))
    #         # 下面是耗时计算完成后的结果处理。
    #         for result in results:
    #             pass
    #     # 返回完成信号
    #     self.finished.emit()
class Tab(QWidget):
    def __init__(self, tab_id):
        super().__init__()
        self.tab_id = tab_id
        self.worker = Worker(tab_id)
        self.worker_thread = QThread()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        self.button = QPushButton(f"Start Task in Tab {self.tab_id}")
        self.button.clicked.connect(self.start_task)
        self.layout.addWidget(self.button)

        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.do_work)
        self.worker.update_signal.connect(self.update_text)
        # 完成之后进行线程退出和关闭，避免资源浪费
        self.worker.finished.connect(self.task_finished)

    def start_task(self):
        self.worker_thread.start()
        print("{}线程开始".format(self.tab_id))

    @Slot(str)
    def update_text(self, text):
        self.text_edit.append(text)

    @Slot()
    def task_finished(self):
        # 槽函数：完成运算之后，该槽函数将刚才创建的线程销毁
        self.worker_thread.quit()
        self.worker_thread.wait()
        print("{}线程结束".format(self.tab_id))

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-processing Example")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        self.tab2 = Tab(2)
        self.tab_widget.addTab(self.tab2, "Tab 2")

        self.tab3 = Tab(3)
        self.tab_widget.addTab(self.tab3, "Tab 3")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
