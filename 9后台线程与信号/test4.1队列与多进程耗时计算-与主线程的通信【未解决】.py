from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QTextBrowser
from PySide2.QtCore import QObject, Signal, Slot
import multiprocessing as mp
import time
import random

class Worker(QObject):
    update_text = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot()
    def start_calculation(self, conn):
        def expensive_calculation(x):
            result = x * x
            time.sleep(random.uniform(0.5, 1.5))  # 模拟耗时操作
            message = f"Process {mp.current_process().name}: Calculated {x} * {x} = {result}"
            conn.send(message)

        with mp.Pool(processes=3) as pool:
            pool.map(expensive_calculation, range(10))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CPU计算")
        self.setGeometry(100, 100, 400, 300)

        self.text_browser = QTextBrowser(self)
        self.text_browser.setGeometry(10, 10, 380, 200)

        self.start_button = QPushButton("开始计算", self)
        self.start_button.setGeometry(150, 220, 100, 30)

        self.parent_conn, self.child_conn = mp.Pipe()
        self.worker = Worker()
        self.worker_thread = mp.Process(target=self.worker.start_calculation, args=(self.child_conn,))
        self.worker_thread.start()

        self.worker.update_text.connect(self.update_text_browser)
        self.start_button.clicked.connect(self.start_calculation)

    def start_calculation(self):
        pass  # 不需要实现该方法，因为计算已经在子进程中进行

    @Slot(str)
    def update_text_browser(self, message):
        self.text_browser.append(message)

    def closeEvent(self, event):
        if self.worker_thread.is_alive():
            self.worker_thread.terminate()
        event.accept()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
