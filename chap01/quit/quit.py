from PyQt4.QtCore import QObject, SIGNAL, SLOT
from PyQt4.QtGui import QApplication, QPushButton
import sys

if __name__ == "__main__":
    app = QApplication (sys.argv)

    button = QPushButton("Quit")

    QObject.connect(button, SIGNAL("clicked()"), app, SLOT("quit()"))
    button.show()
    app.exec_()
