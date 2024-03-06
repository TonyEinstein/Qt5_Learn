from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QObject
from PySide2.QtGui import  QIcon

import traceback

import requests


class HttpClient(QObject):

    def __init__(self):
        QObject.__init__(self)

        # 从 UI 定义中动态 创建一个相应的窗口对象
        self.ui = QUiLoader().load('ui/httpclient.ui')

        # 给 boxMethod 添加选项 GET POST PUT DELETE
        self.ui.boxMethod.addItems(
            ['GET', 'POST', 'PUT', 'DELETE' ])

        # 让 表格控件宽度随着父窗口的缩放自动缩放
        self.ui.headersTable.horizontalHeader().setStretchLastSection(True)
        # 设定第1列的宽度为 180像素
        self.ui.headersTable.setColumnWidth(0, 180)

        # 信号处理：发送请求
        self.ui.buttonSend.clicked.connect(self.sendRequest)
        # 信号处理：添加消息头
        self.ui.buttonAddHeader.clicked.connect(self.addOneHeader)
        # 信号处理：删除消息头
        self.ui.buttonDelHeader.clicked.connect(self.delOneHeader)


    def addOneHeader(self):

        # rowCount = self.ui.headersTable.rowCount()
        # 要插入的行始终是当前行 的下一行
        addRowNumber = self.ui.headersTable.currentRow() + 1
        self.ui.headersTable.insertRow(addRowNumber)

    def delOneHeader(self):

        self.ui.headersTable.removeRow(
            self.ui.headersTable.currentRow()
        )

    def sendRequest(self):

        method = self.ui.boxMethod.currentText()
        url    = self.ui.editUrl.text()
        payload = self.ui.editBody.toPlainText()

        # 获取消息头
        headers = {}
        ht = self.ui.headersTable
        for row in range(ht.rowCount()):
            k = ht.item(row,0).text()
            v = ht.item(row,1).text()
            if k.strip() == '':
                continue
            headers[k] = v

        req = requests.Request(method,
                               url,
                               headers=headers,
                               data=payload
                               )

        prepared = req.prepare()

        self.pretty_print_request(prepared)
        s = requests.Session()

        try:
            r = s.send(prepared)
            self.pretty_print_response(r)
        except:
            self.ui.outputWindow.append(
                traceback.format_exc())


    def pretty_print_request(self,req):

        if req.body == None:
            msgBody = ''
        else:
            msgBody = req.body

        self.ui.outputWindow.append(
            '{}\n{}\n{}\n\n{}'.format(
            '\n\n----------- 发送请求 -----------',
            req.method + ' ' + req.url,
            '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
            msgBody,
        ))

    def pretty_print_response(self,res):
        self.ui.outputWindow.append(
            '{}\nHTTP/1.1 {}\n{}\n\n{}'.format(
            '\n\n----------- 得到响应 -----------',
            res.status_code,
            '\n'.join('{}: {}'.format(k, v) for k, v in res.headers.items()),
            res.text,
        ))

app = QApplication([])
# 加载 icon
app.setWindowIcon(QIcon('ui/logo.png'))
httpClient = HttpClient()
httpClient.ui.show()
app.exec_()