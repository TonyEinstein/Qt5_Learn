from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from ..mdis.ui_subwin2 import Ui_MainWindow


class CSubWindow2(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(CSubWindow2,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = CSubWindow2()
    MainWindow.show()
    sys.exit(app.exec_())