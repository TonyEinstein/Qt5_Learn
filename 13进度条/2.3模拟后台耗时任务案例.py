import sys
import time
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QProgressBar, QPushButton
from PySide2.QtCore import QThread, Signal

class WorkerThread(QThread):
    progress_changed = Signal(int)

    def run(self):
        for i in range(101):
            """
            模拟耗时
            """
            time.sleep(0.1)  # 模拟一个耗时任务
            self.progress_changed.emit(i)  # 发出信号通知进度更新

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Threaded Progress Bar")

        # 创建进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)

        # 创建按钮
        self.button = QPushButton("Start Task")
        self.button.clicked.connect(self.start_task)

        # 创建布局
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.button)

        # 设置中央窗口部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 创建线程对象
        self.worker_thread = WorkerThread()
        self.worker_thread.progress_changed.connect(self.progress_bar.setValue)

    def start_task(self):
        self.worker_thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

"""
在执行运行任务（如文件下载、数据处理等）时，文档条非常有用。我们可以使用线程来执行这些任务，同时在主线程中更新文档条。
解释：
QThread用于执行运行任务，避免阻塞主线程。
通过信号和槽机制，在线程中更新主线程中的QProgressBar。
"""