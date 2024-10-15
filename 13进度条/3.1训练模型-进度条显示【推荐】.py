import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar, QLabel
from PySide2.QtCore import QThread, Signal, Slot
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
import time

# 创建一个训练线程类，用于模型训练
class TrainingThread(QThread):
    progress = Signal(int)  # 用于更新进度条的信号
    finished = Signal()     # 训练结束的信号
    paused = False          # 用于控制训练的暂停
    stop_training = False   # 用于控制训练的结束

    def __init__(self, X_train, y_train):
        super().__init__()
        self.X_train = X_train
        self.y_train = y_train

    def run(self):
        model = SGDClassifier(max_iter=1000, tol=1e-3)
        batch_size = len(self.X_train) // 10  # 将训练分为10批进行

        for i in range(10):
            """
            假如训练粘贴按钮被点下那么将停止线程，点下继续那么将继续训练
            """
            if self.stop_training:
                break
            # 模拟训练
            model.partial_fit(self.X_train[i*batch_size:(i+1)*batch_size], self.y_train[i*batch_size:(i+1)*batch_size], classes=[0, 1, 2])
            self.progress.emit((i+1)*10)  # 更新进度条
            time.sleep(1)  # 模拟训练时间
            while self.paused:  # 如果暂停，保持等待
                self.msleep(100)
        self.finished.emit()

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def stop(self):
        self.stop_training = True

# 创建主窗口类
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("模型训练进度")
        self.layout = QVBoxLayout()

        # 创建标签用于显示状态
        self.label = QLabel("训练状态: 未开始")
        self.layout.addWidget(self.label)

        # 创建进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.layout.addWidget(self.progress_bar)

        # 创建按钮
        self.start_button = QPushButton("开始训练")
        self.pause_button = QPushButton("暂停训练")
        self.resume_button = QPushButton("继续训练")

        # 禁用暂停和继续按钮，直到训练开始
        self.pause_button.setEnabled(False)
        self.resume_button.setEnabled(False)

        # 添加按钮到布局
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.pause_button)
        self.layout.addWidget(self.resume_button)

        self.setLayout(self.layout)

        # 加载数据集并拆分
        data = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

        # 创建训练线程
        self.training_thread = TrainingThread(X_train, y_train)

        # 连接信号和槽
        self.start_button.clicked.connect(self.start_training)
        self.pause_button.clicked.connect(self.pause_training)
        self.resume_button.clicked.connect(self.resume_training)
        self.training_thread.progress.connect(self.update_progress)
        self.training_thread.finished.connect(self.training_finished)

    @Slot()
    def start_training(self):
        self.label.setText("训练状态: 进行中")
        self.start_button.setEnabled(False)
        self.pause_button.setEnabled(True)
        self.resume_button.setEnabled(False)
        self.training_thread.start()

    @Slot()
    def pause_training(self):
        self.label.setText("训练状态: 暂停")
        self.training_thread.pause()
        self.pause_button.setEnabled(False)
        self.resume_button.setEnabled(True)

    @Slot()
    def resume_training(self):
        self.label.setText("训练状态: 继续")
        self.training_thread.resume()
        self.pause_button.setEnabled(True)
        self.resume_button.setEnabled(False)

    @Slot()
    def update_progress(self, value):
        self.progress_bar.setValue(value)

    @Slot()
    def training_finished(self):
        self.label.setText("训练状态: 完成")
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.resume_button.setEnabled(False)

# 主程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
