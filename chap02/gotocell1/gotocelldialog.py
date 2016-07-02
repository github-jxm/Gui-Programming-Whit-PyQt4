#!/usr/bin/env python
#coding=utf-8


from ui_gotocelldialog import Ui_GoToCellDialog
from PyQt4.QtGui import QDialog

class GotocellDialog(QDialog,Ui_GoToCellDialog):
    def __init__(self,parent=None):
        super(GotocellDialog, self).__init__(parent)
        self.setupUi(self)



if __name__ == "__main__":
    from PyQt4.QtGui import QApplication
    import sys
    app = QApplication(sys.argv)

    win = GotocellDialog()

    win.show()
    app.exec_()

