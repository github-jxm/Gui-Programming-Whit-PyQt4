#!/usr/bin/env python
#coding=utf-8
from PyQt4.QtCore import QRegExp, SIGNAL, SLOT

from ui_gotocelldialog import Ui_GoToCellDialog
from PyQt4.QtGui import QDialog, QRegExpValidator


class GotocellDialog(QDialog,Ui_GoToCellDialog):
    def __init__(self,parent=None):
        super(GotocellDialog, self).__init__(parent)
        self.setupUi(self)

        # 允许 一个大写或者小写的字母,后面跟着一个范围1~9的数字,
        # 后面再跟0个,1个或 2个0~9的数字(对于正则表达式的介绍,请查看文档中QRegExp类)
        regExp = QRegExp("[A-Za-z][1-9][0-9]{0,2}")



        self.lineEdit.setValidator(QRegExpValidator(regExp,self))

        self.connect(self.okButton,SIGNAL("clicked()"),
                     self,SLOT("accept()"))
        self.connect(self.cancelButton,SIGNAL("clicked()"),
                     self,SLOT("reject()"))

    #   on_objectName_signalName()
    def on_lineEdit_textChanged(self):
        # QLineEdit.hasAcceptableInput() 使用构造函数设置检验器来判断输入的有效性
        self.okButton.setEnabled(self.lineEdit.hasAcceptableInput());


if __name__ == "__main__":
    from PyQt4.QtGui import QApplication
    import sys
    app = QApplication(sys.argv)

    win = GotocellDialog()

    # win.show()
    win.exec_()
    app.exec_()

