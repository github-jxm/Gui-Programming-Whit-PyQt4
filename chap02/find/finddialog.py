#!/usr/bin/env python
#coding=utf-8

from PyQt4.QtCore import SIGNAL, SLOT, QString,pyqtSlot, QMetaObject, Qt
from PyQt4.QtGui import QDialog, QLabel, QLineEdit
from PyQt4.QtGui import   QCheckBox, QPushButton
from PyQt4.QtGui import QHBoxLayout,QVBoxLayout


class FindDialog(QDialog):
    def __init__(self,parent=None):
        super(FindDialog, self,).__init__(parent)
        self.label = QLabel(str("Find &what:"))
        self.lineEdit = QLineEdit()
        self.label.setBuddy(self.lineEdit)

        self.caseCheckBox = QCheckBox(str("Match &case"))
        self.backwardCheckBox =  QCheckBox(str("Search &backward"))

        self.findButton =  QPushButton(str("&Find"))
        self.findButton.setDefault(True)
        self.findButton.setEnabled(False)

        closeButton =  QPushButton(str("Close"))

        #--------------------------------------------------------
        # 1. 连接的槽 必须 指定  @pyqtSlot(QString)
        self.connect(self.lineEdit, SIGNAL("textChanged(QString)"),
                     self, SLOT("enableFindButton(QString)"))
        # 2. 不必指定 @pyqtSlot(QString)
        # self.connect(self.lineEdit, SIGNAL("textChanged(QString)"),
        #               self.enableFindButton)
        #---------------------------------------------------------

        self.connect(self.findButton, SIGNAL("clicked()"),
                self, SLOT("findClicked()"))
        self.connect(closeButton, SIGNAL("clicked()"),
                self, SLOT("close()"))

        topLeftLayout =  QHBoxLayout()
        topLeftLayout.addWidget(self.label)
        topLeftLayout.addWidget(self.lineEdit)

        leftLayout =  QVBoxLayout()
        leftLayout.addLayout(topLeftLayout)
        leftLayout.addWidget(self.caseCheckBox)
        leftLayout.addWidget(self.backwardCheckBox)

        rightLayout =  QVBoxLayout()
        rightLayout.addWidget(self.findButton)
        rightLayout.addWidget(closeButton)
        rightLayout.addStretch()

        mainLayout =  QHBoxLayout()
        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)
        self.setLayout(mainLayout)


        self.setWindowTitle(str("Find"))
        self.setFixedHeight(self.sizeHint().height())

    @pyqtSlot()
    def findClicked(self):
        text = self.lineEdit.text()
        # Qt.CaseSensitivity cs =
        #         caseCheckBox.isChecked() ? Qt.CaseSensitive
        #                                   : Qt.CaseInsensitive
        #
        cs = None
        if self.caseCheckBox.isChecked() :
            print "case"
            cs = Qt.CaseSensitive
        else:
            print ""
            cs = Qt.CaseInsensitive

        if self.backwardCheckBox.isChecked():
            pass
            # self.emit findPrevious(text, cs)
        else:
            pass
            # self.emit findNext(text, cs)

    @pyqtSlot(QString)
    def enableFindButton(self,text):
        print type(text),":",len(text)
        print(text)
        t = QString(text)
        self.findButton.setEnabled(not t.isEmpty())

