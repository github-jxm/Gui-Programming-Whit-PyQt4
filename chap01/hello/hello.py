#!/usr/bin/env python
#coding=utf-8

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QLabel

import sys

if __name__ == "__main__":

    app = QApplication(sys.argv)
    # label = QLabel("Hello Qt!")
    label = QLabel("<h1>"
                   "<i>Hello</i>"
                   "<font color=red>Qt!<font>"
                   "</h1>")
    label.show()
    app.exec_()
