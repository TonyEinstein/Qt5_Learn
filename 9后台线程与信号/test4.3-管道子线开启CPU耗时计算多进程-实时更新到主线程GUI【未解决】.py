from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QTextBrowser
from PySide2.QtCore import QThread, Signal
import multiprocessing as mp
import time
import random

def worker(pipe, num):
    def expensive_calculation(x):
        result = x * x
        time.sleep(random.uniform(0.5, 1.5))  # 模拟耗时操作
        message = f"Process {mp.current_process().name}: Calculated {x} * {x} = {result}"
        pipe.send(message)

    for i in range(num):
        expensive_calculation(i)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CPU计算")
        self.setGeometry(100, 100, 400, 300)

        self.text_browser = QTextBrowser(self)
        self.text_browser.setGeometry(10, 10, 380, 200)

        self.start_button = QPushButton("开始计算", self)
        self.start_button.setGeometry(150, 220, 100, 30)
        self.start_button.clicked.connect(self.start_calculation)

    def start_calculation(self):
        self.text_browser.clear()

        parent_conn, child_conn = mp.Pipe()
        process = mp.Process(target=worker, args=(child_conn, 10))  # 10为计算次数
        process.start()

        while process.is_alive():
            if parent_conn.poll():
                message = parent_conn.recv()
                self.text_browser.append(message)
            QApplication.processEvents()
            time.sleep(0.1)

        process.join()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
