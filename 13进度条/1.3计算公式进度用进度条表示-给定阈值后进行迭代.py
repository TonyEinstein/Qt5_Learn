import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton, QVBoxLayout, QWidget, QTextBrowser
from PySide2.QtCore import QBasicTimer, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 设置窗口标题和大小
        self.setWindowTitle('次方计算进度条示例')
        self.setGeometry(100, 100, 400, 300)

        # 创建进度条组件
        self.progress_bar = QProgressBar(self)
        # 设置进度条的最小值为1，最大值为10000，表示计算从1次方到10000次方
        self.progress_bar.setMinimum(1)
        self.progress_bar.setMaximum(10000)

        # 创建文本浏览器，用于显示每次计算的结果
        self.text_browser = QTextBrowser(self)

        # 创建按钮组件
        # 开始按钮：点击后开始计算并更新进度条
        self.start_button = QPushButton('开始计算', self)
        self.start_button.clicked.connect(self.start_calculation)  # 绑定按钮点击事件

        # 暂停按钮：点击后暂停计算
        self.pause_button = QPushButton('暂停计算', self)
        self.pause_button.clicked.connect(self.pause_calculation)

        # 继续按钮：点击后继续之前的计算
        self.continue_button = QPushButton('继续计算', self)
        self.continue_button.clicked.connect(self.continue_calculation)

        # 重置按钮：点击后重置进度条和结果显示
        self.reset_button = QPushButton('重置', self)
        self.reset_button.clicked.connect(self.reset_calculation)

        # 布局设置，将各个组件垂直排列在窗口中
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)  # 将进度条加入布局
        layout.addWidget(self.text_browser)  # 将文本输出框加入布局
        layout.addWidget(self.start_button)  # 将开始按钮加入布局
        layout.addWidget(self.pause_button)  # 将暂停按钮加入布局
        layout.addWidget(self.continue_button)  # 将继续按钮加入布局
        layout.addWidget(self.reset_button)  # 将重置按钮加入布局

        # 创建中央窗口部件并设置布局
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 初始化计时器，用于控制计算的进度
        self.timer = QBasicTimer()
        # 初始化计算状态变量
        self.current_exponent = 1  # 当前计算到的次方，初始为1
        self.is_paused = False  # 是否处于暂停状态的标志位

    # 开始计算的函数，启动计时器并开始计算次方
    def start_calculation(self):
        # 检查计时器是否已经在运行，防止重复启动
        if not self.timer.isActive():
            # 启动计时器，间隔时间为1毫秒，触发timerEvent
            self.timer.start(1, self)
            # 禁用开始按钮，防止多次点击
            self.start_button.setEnabled(False)

    # 暂停计算的函数，将暂停标志设置为True
    def pause_calculation(self):
        self.is_paused = True

    # 继续计算的函数，清除暂停标志
    def continue_calculation(self):
        if self.is_paused:
            self.is_paused = False

    # 重置计算的函数，停止计时器，重置进度条和文本框
    def reset_calculation(self):
        self.timer.stop()  # 停止计时器
        self.current_exponent = 1  # 将当前次方重置为1
        self.progress_bar.setValue(1)  # 将进度条重置为1
        self.text_browser.clear()  # 清空文本框
        self.start_button.setEnabled(True)  # 启用开始按钮
        self.is_paused = False  # 重置暂停标志

    # 定时器事件函数，每次计时器触发时执行一次
    def timerEvent(self, event):
        # 如果处于暂停状态，则不执行任何操作
        if self.is_paused:
            return

        # 如果当前次方超过10000（进度最大值），表示计算完成，停止计时器
        if self.current_exponent > 10000:
            self.timer.stop()  # 停止计时器
            self.start_button.setEnabled(True)  # 计算完成后启用开始按钮
            return

        # 实际上计算  current_exponent 的2次方
        result = self.current_exponent**2  # 计算current_exponent的2次方
        # 将计算结果追加到文本框中显示
        self.text_browser.append(f"{self.current_exponent}**2 = {result}")
        # 更新进度条的值，显示当前的进度
        self.progress_bar.setValue(self.current_exponent)
        # 递增当前次方
        self.current_exponent += 1


# 应用程序的主函数，启动Qt应用程序并运行窗口
if __name__ == "__main__":
    # 创建应用程序对象
    app = QApplication(sys.argv)
    # 创建并显示主窗口
    window = MainWindow()
    window.show()
    # 运行应用程序主循环
    sys.exit(app.exec_())
