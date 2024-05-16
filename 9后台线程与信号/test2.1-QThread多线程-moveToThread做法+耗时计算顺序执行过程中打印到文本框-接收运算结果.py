# -*- coding: utf-8 -*-
import sys
import time
import concurrent.futures
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QTabWidget
from PySide2.QtCore import QObject, Signal, Slot, QThread


"""
对test1.0的代码进行细化和封装
"""
def calculate(i):
    result = i * i
    time.sleep(0.5)
    return result

class Worker(QObject):
    # 完成标识
    finished = Signal()
    # 运算过程中的信息返回标识
    resultReady = Signal(int)
    # 运算结束后的信息返回标识
    resultsReady = Signal(list)

    def __init__(self, tab_id):
        super().__init__()
        self.tab_id = tab_id

    @Slot()
    def do_work(self):
        # 可以把运算结果存储在此results列表变量中，可以返回
        results = []
        for i in range(10):
            result = calculate(i)
            results.append(result)
            self.resultReady.emit(result)
        self.resultsReady.emit(results)  # 发送结果列表
        self.finished.emit()

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

        self.worker.resultReady.connect(self.update_text)
        # 下面这个resultsReady信号连接的槽函数handle_results是获取运算结果
        self.worker.resultsReady.connect(self.handle_results)  # 连接新的信号
        # 完成之后进行线程退出和关闭，避免资源浪费
        self.worker.finished.connect(self.task_finished)

    def start_task(self):
        # 由于Worker没有继承QThread，如果用worker.start()是无法开启线程的。需要用QThread实例开启线程。
        self.worker_thread.start()
        print("{}线程开始".format(self.tab_id))

    @Slot(int)
    def update_text(self, result):
        self.text_edit.append(f"Result from Tab {self.tab_id}: {result}")

    @Slot(list)
    def handle_results(self, results):
        # 在此处使用结果列表
        print(f"Results from Tab {self.tab_id}: {results}")
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
