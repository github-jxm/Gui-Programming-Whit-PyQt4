#!/usr/bin/env python
#coding=utf-8

from PyQt4.QtCore import QString, QChar

from PyQt4.QtGui import QDialog, QLayout
from ui_sortdialog import Ui_SortDialog

class SortDialog(QDialog,Ui_SortDialog):
    def __init__(self,parent=None):
        super(SortDialog, self).__init__(parent)
        self.setupUi(self)
        self.secondaryGroupBox.hide()
        self.tertiaryGroupBox.hide()
        self.layout().setSizeConstraint(QLayout.SetFixedSize)

        self.setColumnRange('A', 'Z')

    def  setColumnRange(self, first,  last):
        self.primaryColumnCombo.clear()
        self.secondaryColumnCombo.clear()
        self.tertiaryColumnCombo.clear()

        self.secondaryColumnCombo.addItem(str("None"))
        self.tertiaryColumnCombo.addItem(str("None"))

        self.primaryColumnCombo.setMinimumSize(
                self.secondaryColumnCombo.sizeHint())


        ch = ord(first) # 转换成 数字
        while (ch <= ord(last)):
            self.primaryColumnCombo.addItem(QString(chr(ch)))
            self.secondaryColumnCombo.addItem(QString(chr(ch)))
            self.tertiaryColumnCombo.addItem(QString(chr(ch)))
            ch = ch + 1


if __name__ == "__main__":
    import sys
    from PyQt4.QtGui import QApplication
    app = QApplication(sys.argv)
    dialog = SortDialog()
    dialog.setColumnRange('A', 'M')
    dialog.show()
    app.exec_()
