
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

import requests

from lib.share import SI

class Win_Login:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('login.ui')

        self.ui.btn_login.clicked.connect(self.onSignIn)
        self.ui.edt_password.returnPressed.connect(self.onSignIn)

    def onSignIn(self):
        username = self.ui.edt_username.text().strip()
        password = self.ui.edt_password.text().strip()

        s = requests.Session()
        url = "http://192.168.1.105/api/sign"

        res = s.post(url,json={
            "action" : "signin",
            "username" : username,
            "password" : password
        })

        resObj = res.json()
        if resObj['ret'] != 0:
            QMessageBox.warning(
                self.ui,
                '登录失败',
                resObj['msg'])
            return

        SI.mainWin = Win_Main()
        SI.mainWin.ui.show()

        self.ui.edt_password.setText('')
        self.ui.hide()


class Win_Main :

    def __init__(self):
        self.ui = QUiLoader().load('main.ui')



"""
先是实例化了登录页面，然后登录成功才进行跳转到mian页面
"""

app = QApplication([])
SI.loginWin = Win_Login()
SI.loginWin.ui.show()
app.exec_()