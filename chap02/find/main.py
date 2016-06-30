from PyQt4.QtGui import QApplication
from finddialog import FindDialog
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = FindDialog()
    dialog.show()
    app.exec_()
