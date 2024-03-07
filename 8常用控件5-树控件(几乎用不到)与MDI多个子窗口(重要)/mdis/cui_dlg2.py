from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog

from ..mdis.ui_dlg2 import Ui_Dialog


class Dlg2(QDialog,Ui_Dialog):
    def __init__(self):
        super(Dlg2,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        #此处添加业务代码


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = Dlg2()
    Dialog.show()
    sys.exit(app.exec_())