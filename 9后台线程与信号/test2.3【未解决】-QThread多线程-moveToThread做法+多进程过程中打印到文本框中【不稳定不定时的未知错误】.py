import multiprocessing
import sys
import time
import concurrent.futures
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QTabWidget
from PySide2.QtCore import QObject, Signal, Slot, QThread, QMetaObject, Qt


# 单独的模块 worker.py
# class WorkerSignals(QObject):
#     finished = Signal()
#     update_signal = Signal(str)

class Worker(QObject):
    finished = Signal()
    update_signal = Signal(str)

    def __init__(self, tab_id):
        super().__init__()
        self.tab_id = tab_id

    """
    堵塞主线程的原因：
        1.创建的进程池中的进程数量默认等于机器的CPU核心数，如果耗时任务数量较多，可能会导致进程池中的进程数量过多，从而影响系统性能，导致界面卡顿或无响应。
        2.进程池多进程的子进程无法与主线程进行通信，因为要保证主线程安全。    
    
    可能的解决方法：
        1.限制进程池中的进程数量；
        2.优化耗时任务；
        3.多进程执行完成后再将结果返回，这种做法是无法在执行的期间进行返回信号的。
        4.使用进程间通信（IPC）机制，使用multiprocessing.Queue实现主线程和子进程之间的通信。主线程将查询结果发送到队列，子进程从队列中获取结果并更新GUI。【推荐，但是难度高】
        5.使用回调函数（Callback），将修改calculate函数，使其接受一个回调函数作为参数。子进程在计算完成后调用回调函数，并传递计算结果给主线程。（这种做法是无法在执行的期间进行返回信号的。）
        6.使用定时器（Timer），将使用QTimer定时器在主线程中定期查询子进程的状态，并获取部分计算结果更新GUI。
    """

    # ----------------------------------【1.concurrent.futures.ProcessPoolExecutor()实现进程池用于耗时计算】
    @Slot()
    def do_work(self):
        with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
            print("线程 {} 我被开始执行了".format(self.tab_id))
            """
            executor.map()是ProcessPoolExecutor的一个方法，它接受一个函数和一个可迭代对象作为参数。它将函数应用于可迭代对象的每个元素。
            executor.map()是ProcessPoolExecutor的一个方法，它接受一个函数和一个可迭代对象作为参数。它将函数应用于可迭代对象的每个元素，并返回一个迭代器，该迭代器生成结果。
            """
            # 下面这段代码相当于 for i in range(10) : calculate(i, self.update_signal)
            results = executor.map(lambda i: calculate(i, self.update_signal), range(10))
            print("线程 {} 我被执行完毕了".format(self.tab_id))
            # 下面是耗时计算完成后的结果处理。
            for result in results:
                print(result)
                # self.update_signal.emit(f"Calculating result for {result} ...")
        # 返回完成信号
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

def calculate(i, update_signal):
    # 下面的返回打印信号，是在多进程计算calculate函数期间(计算过程中)返回的。是最难的一种。
    update_signal.emit(f"Calculating result for {i} ...")
    result = i * i
    # QApplication.processEvents()
    print(i,result)
    time.sleep(1)
    return result

# 第一个Tab页类
class Tab1(QWidget):
    def __init__(self,tab_id):
        super().__init__()
        self.tab_id = tab_id
        self.layout = QVBoxLayout(self)

        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        self.button = QPushButton("Start Task in Tab 1")
        self.button.clicked.connect(self.start_task)
        self.layout.addWidget(self.button)

        # 没点击之后这里也会实例化线程，但是没有真正创建。
        self.worker_thread = QThread()
        self.worker = Worker(tab_id)
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.do_work)
        self.worker.update_signal.connect(self.update_text)
        # 完成之后进行线程退出和关闭，避免资源浪费
        self.worker.finished.connect(self.task_finished)

    def start_task(self):
        # 创建线程
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

    def stop_thread(self):
        self.worker_thread.quit()
        self.worker_thread.wait()
        print("关闭界面，{}线程自动退出".format(self.tab_id))

# 第二个Tab页类
class Tab2(QWidget):
    def __init__(self,tab_id):
        super().__init__()
        self.tab_id = tab_id
        self.layout = QVBoxLayout(self)

        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        self.button = QPushButton("Start Task in Tab 2")
        self.button.clicked.connect(self.start_task)
        self.layout.addWidget(self.button)

        self.worker_thread = QThread()
        self.worker = Worker(self.tab_id)
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

    def stop_thread(self):
        self.worker_thread.quit()
        self.worker_thread.wait()
        print("关闭界面，{}线程自动退出".format(self.tab_id))
# 主窗口类
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-threading Example")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        # 实例化并添加第一个Tab页
        self.tab1 = Tab1(tab_id=1)
        self.tab_widget.addTab(self.tab1, "Tab 1")

        # 实例化并添加第二个Tab页
        self.tab2 = Tab2(tab_id=2)
        self.tab_widget.addTab(self.tab2, "Tab 2")

    def closeEvent(self, event):
        """
        closeEvent是QMainWindow本就存在的。是面向对象编程的继承特性的体现。
        在窗口关闭的时候，会自动调用该函数。
        :param event:
        :return:
        """
        # 关闭窗口时，停止所有线程
        self.tab1.stop_thread()
        self.tab2.stop_thread()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())