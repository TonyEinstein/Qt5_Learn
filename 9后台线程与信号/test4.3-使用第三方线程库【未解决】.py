import sys
import concurrent.futures
import multiprocessing as mp
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CPU Intensive Computation")

        # 创建主界面小部件
        main_widget = QWidget()
        layout = QVBoxLayout()

        # 创建开始计算按钮
        self.start_button = QPushButton("Start Computation")
        self.start_button.clicked.connect(self.start_computation)
        layout.addWidget(self.start_button)

        # 创建文本框
        self.text_box = QTextEdit()
        layout.addWidget(self.text_box)

        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def start_computation(self):
        # 在按钮点击时启动线程池和进程池
        with concurrent.futures.ThreadPoolExecutor() as thread_pool:
            with concurrent.futures.ProcessPoolExecutor() as process_pool:
                futures = [process_pool.submit(self.compute_square, i) for i in range(10)]
                for future in concurrent.futures.as_completed(futures):
                    try:
                        result = future.result()
                        self.text_box.append(result)
                    except Exception as e:
                        print(f"Error: {e}")

    def compute_square(self, x):
        # CPU 密集型计算
        result = x * x
        return f"Process {mp.current_process().name}: Calculated {x} * {x} = {result}"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())