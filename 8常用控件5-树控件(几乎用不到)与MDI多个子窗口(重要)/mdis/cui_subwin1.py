from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from ..mdis.ui_subwin1 import Ui_MainWindow


class CSubWindow1(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(CSubWindow1,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = CSubWindow1()
    MainWindow.show()
    sys.exit(app.exec_())