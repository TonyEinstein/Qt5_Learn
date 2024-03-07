from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMdiArea, QMainWindow, QMdiSubWindow, QPlainTextEdit

from ..mdis.cui_dlg1 import Dlg1
from ..mdis.cui_dlg2 import Dlg2
from ..mdis.cui_subwin1 import CSubWindow1
from ..mdis.cui_subwin2 import CSubWindow2
from ..mdis.ui_main import Ui_MainWindow



class Cui_main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Cui_main, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.dlg1=Dlg1()
        self.dlg2 =Dlg2()
        self.subwin1=CSubWindow1()
        self.subwin2=CSubWindow2()
        self.actiondlg1.triggered.connect(self.onDlg1)
        self.actiondlg2.triggered.connect(self.onDlg2)
        self.actionsubwin1.triggered.connect(self.onSubwin1)
        self.actionsubwin2.triggered.connect(self.onSubwin2)

    def initUi(self):
        pass
    def newSub(self):
        newDoc = QMdiSubWindow(self)               #1.创建子窗口
        newDoc.setWindowTitle('新文档 ' + str(self.newDocIndex))
        self.newDocIndex += 1
        newDoc.setWidget(QPlainTextEdit(newDoc))
        self.mdiArea.addSubWindow(newDoc)         #2.添加实例到MDI区域
        newDoc.show()                             #3.显示

    def onSubwin1(self):
        # 把win加载进MDI中
        print("onSubwin1")
        self.mdiArea.addSubWindow(self.subwin1)
        self.subwin1.show()
    def onSubwin2(self):
        print("onSubwin2")
        self.mdiArea.addSubWindow(self.subwin2)
        self.subwin2.show()
    def onDlg1(self):
        print("onDlg1")     #   self.dlg1.show()
        self.mdiArea.addSubWindow(self.dlg1)
        self.dlg1.show()
    def onDlg2(self):
        print("onDlg2")
        self.mdiArea.addSubWindow(self.dlg2)
        self.dlg2.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Cui_main()
    MainWindow.show()
    sys.exit(app.exec_())