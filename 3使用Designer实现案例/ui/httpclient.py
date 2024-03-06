# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'httpclient.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HttpClient(object):
    def setupUi(self, HttpClient):
        HttpClient.setObjectName("HttpClient")
        HttpClient.resize(900, 611)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HttpClient.sizePolicy().hasHeightForWidth())
        HttpClient.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        HttpClient.setFont(font)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(HttpClient)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.boxMethod = QtWidgets.QComboBox(HttpClient)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.boxMethod.setFont(font)
        self.boxMethod.setEditable(False)
        self.boxMethod.setObjectName("boxMethod")
        self.horizontalLayout.addWidget(self.boxMethod)
        self.editUrl = QtWidgets.QLineEdit(HttpClient)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.editUrl.setFont(font)
        self.editUrl.setObjectName("editUrl")
        self.horizontalLayout.addWidget(self.editUrl)
        self.buttonSend = QtWidgets.QPushButton(HttpClient)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.buttonSend.setFont(font)
        self.buttonSend.setObjectName("buttonSend")
        self.horizontalLayout.addWidget(self.buttonSend)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(HttpClient)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(HttpClient)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.buttonAddHeader = QtWidgets.QPushButton(HttpClient)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonAddHeader.sizePolicy().hasHeightForWidth())
        self.buttonAddHeader.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.buttonAddHeader.setFont(font)
        self.buttonAddHeader.setObjectName("buttonAddHeader")
        self.horizontalLayout_2.addWidget(self.buttonAddHeader)
        self.buttonDelHeader = QtWidgets.QPushButton(HttpClient)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDelHeader.sizePolicy().hasHeightForWidth())
        self.buttonDelHeader.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.buttonDelHeader.setFont(font)
        self.buttonDelHeader.setObjectName("buttonDelHeader")
        self.horizontalLayout_2.addWidget(self.buttonDelHeader)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.headersTable = QtWidgets.QTableWidget(HttpClient)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.headersTable.setFont(font)
        self.headersTable.setObjectName("headersTable")
        self.headersTable.setColumnCount(2)
        self.headersTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.headersTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(221, 221, 221))
        self.headersTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(221, 221, 221))
        self.headersTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.headersTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.headersTable.setItem(0, 1, item)
        self.verticalLayout_2.addWidget(self.headersTable)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(HttpClient)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(HttpClient)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.editBody = QtWidgets.QTextEdit(HttpClient)
        self.editBody.setEnabled(True)
        self.editBody.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.editBody.setObjectName("editBody")
        self.verticalLayout.addWidget(self.editBody)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.line_3 = QtWidgets.QFrame(HttpClient)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.outputWindow = QtWidgets.QTextEdit(HttpClient)
        self.outputWindow.setObjectName("outputWindow")
        self.verticalLayout_3.addWidget(self.outputWindow)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.buttonClearLog = QtWidgets.QPushButton(HttpClient)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonClearLog.sizePolicy().hasHeightForWidth())
        self.buttonClearLog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.buttonClearLog.setFont(font)
        self.buttonClearLog.setObjectName("buttonClearLog")
        self.horizontalLayout_7.addWidget(self.buttonClearLog)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.retranslateUi(HttpClient)
        self.buttonClearLog.clicked.connect(self.outputWindow.clear)
        QtCore.QMetaObject.connectSlotsByName(HttpClient)

    def retranslateUi(self, HttpClient):
        _translate = QtCore.QCoreApplication.translate
        HttpClient.setWindowTitle(_translate("HttpClient", "HTTP 接口测试"))
        self.editUrl.setText(_translate("HttpClient", "http://www.baidu.com"))
        self.editUrl.setPlaceholderText(_translate("HttpClient", "请输入URL"))
        self.buttonSend.setText(_translate("HttpClient", "发送"))
        self.label.setText(_translate("HttpClient", "消息头"))
        self.buttonAddHeader.setText(_translate("HttpClient", "+"))
        self.buttonDelHeader.setText(_translate("HttpClient", "-"))
        item = self.headersTable.verticalHeaderItem(0)
        item.setText(_translate("HttpClient", "1"))
        item = self.headersTable.horizontalHeaderItem(0)
        item.setText(_translate("HttpClient", "名称"))
        item = self.headersTable.horizontalHeaderItem(1)
        item.setText(_translate("HttpClient", "值"))
        __sortingEnabled = self.headersTable.isSortingEnabled()
        self.headersTable.setSortingEnabled(False)
        item = self.headersTable.item(0, 0)
        item.setText(_translate("HttpClient", "Content-Type"))
        item = self.headersTable.item(0, 1)
        item.setText(_translate("HttpClient", "application/x-www-form-urlencoded"))
        self.headersTable.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("HttpClient", "消息体"))
        self.buttonClearLog.setText(_translate("HttpClient", "清除"))
