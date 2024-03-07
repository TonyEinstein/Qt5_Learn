import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar,
                             QMenu, QAction, QActionGroup, QToolBar,
                             QStyle, QToolButton, QMdiArea,
                             QMdiSubWindow, QPlainTextEdit,
                             QFileDialog, QMessageBox)
class DemoMdi(QMainWindow):
    def __init__(self, parent=None):
        super(DemoMdi, self).__init__(parent)

        # 设置窗口标题
        self.setWindowTitle('实战PyQt5: MDI多文档接口程序 演示')
        # 设置窗口大小
        self.resize(480, 360)
        self.initUi()

    def initUi(self):
        self.initMenuBar()
        self.initToolBar()
        self.mdiArea = QMdiArea(self)
        self.setCentralWidget(self.mdiArea)
        self.newDocIndex = 1


    def initMenuBar(self):
        menuBar = self.menuBar()
        style = QApplication.style()

        # ==== 文件 ====#
        fileMenu = menuBar.addMenu('文件')

        # 新建一个文档
        aFileNew = QAction('新建文档', self)
        aFileNew.setIcon(style.standardIcon(QStyle.SP_FileIcon))
        aFileNew.triggered.connect(self.onFileNew)
        fileMenu.addAction(aFileNew)

        # 打开一个文档
        aFileOpen = QAction('打开文档', self)
        aFileOpen.setIcon(style.standardIcon(QStyle.SP_DialogOpenButton))
        aFileOpen.triggered.connect(self.onFileOpen)
        fileMenu.addAction(aFileOpen)

        # 关闭一个文档
        aFileCloseAll = QAction('关闭全部', self)
        aFileCloseAll.setIcon(style.standardIcon(QStyle.SP_DialogCloseButton))
        aFileOpen.triggered.connect(self.onFileCloseAll)
        fileMenu.addAction(aFileCloseAll)

        # 添加分割线
        fileMenu.addSeparator()

        # 触发的是动作
        aFileExit = QAction('退出', self)
        aFileExit.triggered.connect(self.close)
        fileMenu.addAction(aFileExit)

        # ==== 编辑 ====#
        editMenu = menuBar.addMenu('编辑')

        # 剪切
        aEditCut = QAction('剪切', self)
        aEditCut.setIcon(QIcon(':/ico/cut.png'))
        aEditCut.triggered.connect(self.onEditCut)
        editMenu.addAction(aEditCut)

        # 复制
        aEditCopy = QAction('复制', self)
        aEditCopy.setIcon(QIcon(':/ico/copy.png'))
        aEditCopy.triggered.connect(self.onEditCopy)
        editMenu.addAction(aEditCopy)

        # 粘贴
        aEditPaste = QAction('粘贴', self)
        aEditPaste.setIcon(QIcon(':/ico/paste.png'))
        aEditPaste.triggered.connect(self.onEditPaste)
        editMenu.addAction(aEditPaste)

        # ==== 窗口排列方式 ====#
        windowMenu = menuBar.addMenu('窗口')
        # 子窗口模式
        aWndSubView = QAction('子窗口模式', self)
        aWndSubView.triggered.connect(lambda: self.onWinowdMode(0))
        windowMenu.addAction(aWndSubView)
        # 标签页模式
        aWndTab = QAction('标签页模式', self)
        aWndTab.triggered.connect(lambda: self.onWinowdMode(1))
        windowMenu.addAction(aWndTab)

        windowMenu.addSeparator()

        # 平铺模式
        aWndTile = QAction('平铺模式', self)
        aWndTile.triggered.connect(lambda: self.onWinowdMode(2))
        windowMenu.addAction(aWndTile)
        # 窗口级联模式
        aWndCascade = QAction('窗口级联模式', self)
        aWndCascade.triggered.connect(lambda: self.onWinowdMode(3))
        windowMenu.addAction(aWndCascade)

    def initToolBar(self):
        toolBar = self.addToolBar('')
        style = QApplication.style()

        min_width = 64

        btnFileNew = QToolButton(self)
        btnFileNew.setText('新建文档')
        btnFileNew.setMinimumWidth(min_width)
        btnFileNew.setIcon(style.standardIcon(QStyle.SP_FileIcon))
        btnFileNew.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnFileNew.clicked.connect(self.onFileNew)
        toolBar.addWidget(btnFileNew)

        btnFileOpen = QToolButton(self)
        btnFileOpen.setText('打开文档')
        btnFileOpen.setMinimumWidth(min_width)
        btnFileOpen.setIcon(style.standardIcon(QStyle.SP_DialogOpenButton))
        btnFileOpen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnFileOpen.clicked.connect(self.onFileOpen)
        toolBar.addWidget(btnFileOpen)

        btnFileCloseAll = QToolButton(self)
        btnFileCloseAll.setText('关闭全部')
        btnFileCloseAll.setMinimumWidth(min_width)
        btnFileCloseAll.setIcon(style.standardIcon(QStyle.SP_DialogCloseButton))
        btnFileCloseAll.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnFileCloseAll.clicked.connect(self.onFileCloseAll)
        toolBar.addWidget(btnFileCloseAll)

        toolBar.addSeparator()

        btnEditCut = QToolButton(self)
        btnEditCut.setText('剪切')
        btnEditCut.setMinimumWidth(64)
        btnEditCut.setIcon(QIcon(':/ico/cut.png'))
        btnEditCut.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnEditCut.clicked.connect(self.onEditCut)
        toolBar.addWidget(btnEditCut)

        btnEditCopy = QToolButton(self)
        btnEditCopy.setText('复制')
        btnEditCopy.setMinimumWidth(64)
        btnEditCopy.setIcon(QIcon(':/ico/copy.png'))
        btnEditCopy.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnEditCopy.clicked.connect(self.onEditCopy)
        toolBar.addWidget(btnEditCopy)

        btnEditPaste = QToolButton(self)
        btnEditPaste.setText('粘贴')
        btnEditPaste.setMinimumWidth(64)
        btnEditPaste.setIcon(QIcon(':/ico/paste.png'))
        btnEditPaste.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnEditPaste.clicked.connect(self.onEditPaste)
        toolBar.addWidget(btnEditPaste)
    def msgCritical(self, strInfo):
        dlg = QMessageBox(self)
        dlg.setIcon(QMessageBox.Critical)
        dlg.setText(strInfo)
        dlg.show()

    def onFileNew(self):
        newDoc = QMdiSubWindow(self)
        newDoc.setWindowTitle('新文档 ' + str(self.newDocIndex))
        self.newDocIndex += 1
        newDoc.setWidget(QPlainTextEdit(newDoc))
        self.mdiArea.addSubWindow(newDoc)
        newDoc.show()

    def onFileOpen(self):
        path, _ = QFileDialog.getOpenFileName(self, '打开文件', '', '文本文件 (*.txt)')
        if path:
            try:
                with open(path, 'rU') as f:
                    text = f.read()
            except Exception as e:
                self.msgCritical(str(e))
            else:
                openDoc = QMdiSubWindow(self)
                openDoc.setWindowTitle(path)
                txtEdit = QPlainTextEdit(openDoc)
                txtEdit.setPlainText(text)
                openDoc.setWidget(txtEdit)
                self.mdiArea.addSubWindow(openDoc)
                openDoc.show()

    def onFileCloseAll(self):
        self.mdiArea.closeAllSubWindows()

    def onEditCut(self):
        txtEdit = self.mdiArea.activeSubWindow().widget()
        txtEdit.cut()

    def onEditCopy(self):
        txtEdit = self.mdiArea.activeSubWindow().widget()
        txtEdit.copy()

    def onEditPaste(self):
        txtEdit = self.mdiArea.activeSubWindow().widget()
        txtEdit.paste()

    def onWinowdMode(self, index):
        if index == 3:
            self.mdiArea.cascadeSubWindows()
        elif index == 2:
            self.mdiArea.tileSubWindows()
        elif index == 1:
            self.mdiArea.setViewMode(QMdiArea.TabbedView)
        else:
            self.mdiArea.setViewMode(QMdiArea.SubWindowView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoMdi()
    window.show()
    sys.exit(app.exec())