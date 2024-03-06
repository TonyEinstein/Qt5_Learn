from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader
import sys

main_win = None
login_win = None
class LoginWin:

    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('ui/login.ui')
        self.ui.btn_login.clicked.connect(self.onLogin)

    def onLogin(self):
        global main_win
        # 实例化另外一个窗口
        main_win = Window_Main()
        # 显示新窗口
        main_win.ui.show()
        # 关闭自己
        self.ui.hide()
        # self.ui.close()



class Window_Main:
    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('ui/main.ui')
        self.ui.loginpushButton.clicked.connect(self.backLogin)

    def backLogin(self):
        global login_win
        # 实例化另外一个窗口
        login_win = LoginWin()
        # 显示新窗口
        login_win.ui.show()
        # 关闭自己
        self.ui.close()

"""
如果经常要在两个窗口来回跳转，可以使用 hide() 方法 隐藏窗口， 而不是 closes() 方法关闭窗口。
这样还有一个好处：被隐藏的窗口再次显示时，原来的操作内容还保存着，不会消失。
"""

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wm = LoginWin()
    wm.ui.show()
    sys.exit(app.exec_())