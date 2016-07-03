#!/usr/bin/env python
#coding=utf-8

#include "finddialog.h"
from PyQt4.QtCore import SIGNAL, SLOT, pyqtSlot
from PyQt4.QtGui import QMainWindow, QIcon, QAction, QKeySequence
from finddialog import FindDialog
from gotocelldialog import GotocellDialog
from sortdialog import SortDialog

#include "gotocelldialog.h"
#include "mainwindow.h"
#include "sortdialog.h"
#include "spreadsheet.h"


import spreadsheet_rc

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        # spreadsheet = new Spreadsheet
        # setCentralWidget(spreadsheet)
        self.setWindowIcon(QIcon(":/images/icon.png"))
        self.setCurrentFile("")

        # ----------- 数据 -------------
        self.spreadsheet = None
        self.findDialog = None
        self.locationLabel=None
        self.formulaLabel = None
        self.recentFiles = None # QStringList recentFiles;
        self.curFile = None# QString curFile;

        self.MaxRecentFiles = 5
        self.recentFileActions = [None]*self.MaxRecentFiles
        #
        self.separatorAction = None
        #
        self.fileMenu = None
        self.editMenu = None
        self.selectSubMenu = None
        self.toolsMenu = None
        self.optionsMenu = None
        self.helpMenu = None
        self.fileToolBar = None
        self.editToolBar = None
        self.newAction = None
        self.openAction = None
        self.saveAction = None
        self.saveAsAction = None
        self.exitAction = None
        self.cutAction = None
        self.copyAction = None
        self.pasteAction = None
        self.deleteAction = None
        self.selectRowAction = None
        self.selectColumnAction = None
        self.selectAllAction = None
        self.findAction = None
        self.goToCellAction = None
        self.recalculateAction = None
        self.sortAction = None
        self.showGridAction = None
        self.autoRecalcAction = None
        self.aboutAction = None
        self.aboutQtAction = None


        self.createActions()
        self.createMenus()

    def closeEvent(self,event):
        if (self.okToContinue()):
            self.writeSettings()
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()
    def newFile(self):
        if (self.okToContinue()) :
            pass
            # spreadsheet.clear()
            # setCurrentFile("")

    @pyqtSlot()
    def open(self):
        #
        # if (okToContinue())
        #     QString fileName = QFileDialog.getOpenFileName(self,
        #                                tr("Open Spreadsheet"), ".",
        #                                tr("Spreadsheet files (*.sp)"))
        #     if (!fileName.isEmpty())
        #         loadFile(fileName)
        #
        pass

    @pyqtSlot()
    def save(self):
        print "save--------------"
        pass
        # if (curFile.isEmpty()):
        #     return saveAs()
        # else:
        #     return saveFile(curFile)

    @pyqtSlot()
    def saveAs(self):
        pass
        # QString fileName = QFileDialog.getSaveFileName(self,
        #                            tr("Save Spreadsheet"), ".",
        #                            tr("Spreadsheet files (*.sp)"))
        # if (fileName.isEmpty())
        #     return false
        #
        # return saveFile(fileName)

    @pyqtSlot()
    def find(self):
        if (self.findDialog == None):
            self.findDialog = FindDialog(self)
        #     connect(findDialog, SIGNAL(findNext(const QString &,
        #                                         Qt.CaseSensitivity)),
        #             spreadsheet, SLOT(findNext(const QString &,
        #                                        Qt.CaseSensitivity)))
        #     connect(findDialog, SIGNAL(findPrevious(const QString &,
        #                                             Qt.CaseSensitivity)),
        #             spreadsheet, SLOT(findPrevious(const QString &,
        #                                            Qt.CaseSensitivity)))
        #
        # self.findDialog.show()
        # self.findDialog.raise()
        # self.findDialog.activateWindow()
        pass

    def goToCell(self):
        # GoToCellDialog dialog(self)
        # if (dialog.exec())
        #     QString str = dialog.lineEdit.text().toUpper()
        #     spreadsheet.setCurrentCell(str.mid(1).toInt() - 1,
        #                                 str[0].unicode() - 'A')
        #
        pass

    @pyqtSlot()
    def sort(self):
        #
        # SortDialog dialog(self)
        # QTableWidgetSelectionRange range = spreadsheet.selectedRange()
        # dialog.setColumnRange('A' + range.leftColumn(),
        #                       'A' + range.rightColumn())
        #
        # if (dialog.exec())
        #     SpreadsheetCompare compare
        #     compare.keys[0] =
        #           dialog.primaryColumnCombo.currentIndex()
        #     compare.keys[1] =
        #           dialog.secondaryColumnCombo.currentIndex() - 1
        #     compare.keys[2] =
        #           dialog.tertiaryColumnCombo.currentIndex() - 1
        #     compare.ascending[0] =
        #           (dialog.primaryOrderCombo.currentIndex() == 0)
        #     compare.ascending[1] =
        #           (dialog.secondaryOrderCombo.currentIndex() == 0)
        #     compare.ascending[2] =
        #           (dialog.tertiaryOrderCombo.currentIndex() == 0)
        #     spreadsheet.sort(compare)
        pass

    @pyqtSlot()
    def about(self):
        pass
        # QMessageBox.about(self, str("About Spreadsheet"),
        #         str("<h2>Spreadsheet 1.1</h2>"
        #            "<p>Copyright &copy 2008 Software Inc."
        #            "<p>Spreadsheet is a small application that "
        #            "demonstrates QAction, QMainWindow, QMenuBar, "
        #            "QStatusBar, QTableWidget, QToolBar, and many other "
        #            "Qt classes."))

    @pyqtSlot()
    def openRecentFile(self):
        pass
        # if (okToContinue()):
        #     QAction *action = qobject_cast<QAction *>(sender())
        #     if (action)
        #         loadFile(action.data().toString())


    @pyqtSlot()
    def updateStatusBar(self):
        pass
        #
        # locationLabel.setText(spreadsheet.currentLocation())
        # formulaLabel.setText(spreadsheet.currentFormula())

    def spreadsheetModified(self):
        pass
        #
        # setWindowModified(true)
        # updateStatusBar()
        #

    # 创建 Actions
    def createActions(self):

        self.newAction = QAction(str("&New"), self)
        self.newAction.setIcon(QIcon(":/images/new.png"))
        self.newAction.setShortcut(QKeySequence.New)
        self.newAction.setStatusTip(str("Create a new spreadsheet file"))
        self.connect(self.newAction, SIGNAL("triggered()"), self, SLOT("newFile()"))

        self.openAction = QAction(str("&Open..."), self)
        self.openAction.setIcon(QIcon(":/images/open.png"))
        self.openAction.setShortcut(QKeySequence.Open)
        self.openAction.setStatusTip(str("Open an existing spreadsheet file"))
        self.connect(self.openAction, SIGNAL("triggered()"), self, SLOT("open()"))

        self.saveAction = QAction(str("&Save"), self)
        self.saveAction.setIcon(QIcon(":/images/save.png"))
        self.saveAction.setShortcut(QKeySequence.Save)
        self.saveAction.setStatusTip(str("Save the spreadsheet to disk"))
        self.connect(self.saveAction, SIGNAL("triggered()"), self, SLOT("save()"))

        self.saveAsAction =  QAction(str("Save &As..."), self)
        self.saveAsAction.setStatusTip(str("Save the spreadsheet under a name"))
        self.connect(self.saveAsAction, SIGNAL("triggered()"), self, SLOT("saveAs()"))

        for i in range(self.MaxRecentFiles):
            self. recentFileActions[i] =  QAction(self)
            self.recentFileActions[i].setVisible(False)
            self.connect(self.recentFileActions[i], SIGNAL("triggered()"),
                    self, SLOT("openRecentFile()"))

        self.exitAction =  QAction(str("E&xit"), self)
        self.exitAction.setShortcut(str("Ctrl+Q"))
        self.exitAction.setStatusTip(str("Exit the application"))
        self.connect(self.exitAction, SIGNAL("triggered()"), self, SLOT("close()"))
        # self.connect(self.exitAction, SIGNAL("triggered()"), self.close)

        self.cutAction =  QAction(str("Cu&t"), self)
        self.cutAction.setIcon(QIcon(":/images/cut.png"))
        self.cutAction.setShortcut(QKeySequence.Cut)
        self.cutAction.setStatusTip(str("Cut the current selection's contents "
                                   "to the clipboard"))
        # self.connect(cutAction, SIGNAL("triggered()"), spreadsheet, SLOT("cut()"))

        self.copyAction =  QAction(str("&Copy"), self)
        self.copyAction.setIcon(QIcon(":/images/copy.png"))
        self.copyAction.setShortcut(QKeySequence.Copy)
        self.copyAction.setStatusTip(str("Copy the current selection's contents "
                                    "to the clipboard"))
        # self.connect(copyAction, SIGNAL("triggered()"), spreadsheet, SLOT(copy()))

        self.pasteAction =  QAction(str("&Paste"), self)
        self.pasteAction.setIcon(QIcon(":/images/paste.png"))
        self.pasteAction.setShortcut(QKeySequence.Paste)
        self.pasteAction.setStatusTip(str("Paste the clipboard's contents into "
                                     "the current selection"))
        # self.connect(pasteAction, SIGNAL("triggered()"),
        #         spreadsheet, SLOT(paste()))

        self.deleteAction =  QAction(str("&Delete"), self)
        self.deleteAction.setShortcut(QKeySequence.Delete)
        self.deleteAction.setStatusTip(str("Delete the current selection's "
                                      "contents"))
        # self.connect(deleteAction, SIGNAL("triggered()"),
        #         spreadsheet, SLOT(del()))

        self.selectRowAction =  QAction(str("&Row"), self)
        self.selectRowAction.setStatusTip(str("Select all the cells in the "
                                         "current row"))
        # self.connect(selectRowAction, SIGNAL("triggered()"),
        #         spreadsheet, SLOT(selectCurrentRow()))

        self.selectColumnAction =  QAction(str("&Column"), self)
        self.selectColumnAction.setStatusTip(str("Select all the cells in the "
                                            "current column"))
        # self.connect(selectColumnAction, SIGNAL("triggered()"),
        #         spreadsheet, SLOT(selectCurrentColumn()))
        #
        self.selectAllAction =  QAction(str("&All"), self)
        self.selectAllAction.setShortcut(QKeySequence.SelectAll)
        self.selectAllAction.setStatusTip(str("Select all the cells in the "
                                         "spreadsheet"))
        # self.connect(selectAllAction, SIGNAL("triggered()"),
        #         spreadsheet, SLOT(selectAll()))

        self.findAction =  QAction(str("&Find..."), self)
        self.findAction.setIcon(QIcon(":/images/find.png"))
        self.findAction.setShortcut(QKeySequence.Find)
        self.findAction.setStatusTip(str("Find a matching cell"))
        self.connect(self.findAction, SIGNAL("triggered()"), self, SLOT("find()"))

        self.goToCellAction =  QAction(str("&Go to Cell..."), self)
        self.goToCellAction.setIcon(QIcon(":/images/gotocell.png"))
        self.goToCellAction.setShortcut(str("Ctrl+G"))
        self.goToCellAction.setStatusTip(str("Go to the specified cell"))
        # self.connect(goToCellAction, SIGNAL("triggered()"),
        #         self, SLOT(goToCell()))

        self.recalculateAction =  QAction(str("&Recalculate"), self)
        self.recalculateAction.setShortcut(str("F9"))
        self.recalculateAction.setStatusTip(str("Recalculate all the "
                                           "spreadsheet's formulas"))
        # self.connect(recalculateAction, SIGNAL("triggered()"),
        #         spreadsheet, SLOT(recalculate()))

        self.sortAction =  QAction(str("&Sort..."), self)
        self.sortAction.setStatusTip(str("Sort the selected cells or all the "
                                    "cells"))
        self.connect(self.sortAction, SIGNAL("triggered()"), self, SLOT("sort()"))

        self.showGridAction =  QAction(str("&Show Grid"), self)
        self.showGridAction.setCheckable(True)
        # self.showGridAction.setChecked(spreadsheet.showGrid())
        self.showGridAction.setStatusTip(str("Show or hide the spreadsheet's "
                                        "grid"))
        # self.connect(showGridAction, SIGNAL("toggled(bool)"),
        #         spreadsheet, SLOT(setShowGrid(bool)))

    # #if QT_VERSION < 0x040102
    #     // workaround for a QTableWidget bug in Qt 4.1.1
    #     self.connect(showGridAction, SIGNAL(toggled(bool)),
    #             spreadsheet.viewport(), SLOT(update()))
    # #endif

        self.autoRecalcAction =  QAction(str("&Auto-Recalculate"), self)
        self.autoRecalcAction.setCheckable(True)
        # self.autoRecalcAction.setChecked(spreadsheet.autoRecalculate())
        self.autoRecalcAction.setStatusTip(str("Switch auto-recalculation on or "
                                          "off"))
    #     self.connect(autoRecalcAction, SIGNAL(toggled(bool)),
    #             spreadsheet, SLOT(setAutoRecalculate(bool)))

        self.aboutAction =  QAction(str("&About"), self)
        self.aboutAction.setStatusTip(str("Show the application's About box"))
        self.connect(self.aboutAction, SIGNAL("triggered()"), self, SLOT("about()"))

        self.aboutQtAction =  QAction(str("About &Qt"), self)
        self.aboutQtAction.setStatusTip(str("Show the Qt library's About box"))
        # self.connect(aboutQtAction, SIGNAL("triggered()"), qApp, SLOT(aboutQt()))

    # 创建 菜单栏
    def createMenus(self):

        self.fileMenu = self.menuBar().addMenu(str("&File"))
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.saveAsAction)
        separatorAction = self.fileMenu.addSeparator()

        for i in range(self.MaxRecentFiles):
             self.fileMenu.addAction(self.recentFileActions[i])

        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)


        self.editMenu = self.menuBar().addMenu(str("&Edit"))
        self.editMenu.addAction(self.cutAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addAction(self.deleteAction)

        self.selectSubMenu = self.editMenu.addMenu(str("&Select"))
        self.selectSubMenu.addAction(self.selectRowAction)
        self.selectSubMenu.addAction(self.selectColumnAction)
        self.selectSubMenu.addAction(self.selectAllAction)

        self.editMenu.addSeparator()
        self.editMenu.addAction(self.findAction)
        self.editMenu.addAction(self.goToCellAction)

        self.toolsMenu = self.menuBar().addMenu(str("&Tools"))
        self.toolsMenu.addAction(self.recalculateAction)
        self.toolsMenu.addAction(self.sortAction)

        self.optionsMenu = self.menuBar().addMenu(str("&Options"))
        self.optionsMenu.addAction(self.showGridAction)
        self.optionsMenu.addAction(self.autoRecalcAction)

        self.menuBar().addSeparator()

        helpMenu = self.menuBar().addMenu(str("&Help"))
        helpMenu.addAction(self.aboutAction)
        helpMenu.addAction(self.aboutQtAction)


    def createContextMenu(self):
        pass
        #
        # spreadsheet.addAction(cutAction)
        # spreadsheet.addAction(copyAction)
        # spreadsheet.addAction(pasteAction)
        # spreadsheet.setContextMenuPolicy(Qt.ActionsContextMenu)
        #

    def createToolBars(self):
        #
        # fileToolBar = addToolBar(tr("&File"))
        # fileToolBar.addAction(newAction)
        # fileToolBar.addAction(openAction)
        # fileToolBar.addAction(saveAction)
        #
        # editToolBar = addToolBar(tr("&Edit"))
        # editToolBar.addAction(cutAction)
        # editToolBar.addAction(copyAction)
        # editToolBar.addAction(pasteAction)
        # editToolBar.addSeparator()
        # editToolBar.addAction(findAction)
        # editToolBar.addAction(goToCellAction)
        #
        pass

    def createStatusBar(self):
        #
        # locationLabel = new QLabel(" W999 ")
        # locationLabel.setAlignment(Qt.AlignHCenter)
        # locationLabel.setMinimumSize(locationLabel.sizeHint())
        #
        # formulaLabel = new QLabel
        # formulaLabel.setIndent(3)
        #
        # statusBar().addWidget(locationLabel)
        # statusBar().addWidget(formulaLabel, 1)
        #
        # connect(spreadsheet, SIGNAL(currentCellChanged(int, int, int, int)),
        #         self, SLOT(updateStatusBar()))
        # connect(spreadsheet, SIGNAL(modified()),
        #         self, SLOT(spreadsheetModified()))
        #
        # updateStatusBar()
        #
        pass

    def readSettings(self):
        pass
        # QSettings settings("Software Inc.", "Spreadsheet")
        #
        # restoreGeometry(settings.value("geometry").toByteArray())
        #
        # recentFiles = settings.value("recentFiles").toStringList()
        # updateRecentFileActions()
        #
        # bool showGrid = settings.value("showGrid", true).toBool()
        # showGridAction.setChecked(showGrid)
        #
        # bool autoRecalc = settings.value("autoRecalc", true).toBool()
        # autoRecalcAction.setChecked(autoRecalc)
        #

    def writeSettings(self):
        #
        # QSettings settings("Software Inc.", "Spreadsheet")
        #
        # settings.setValue("geometry", saveGeometry())
        # settings.setValue("recentFiles", recentFiles)
        # settings.setValue("showGrid", showGridAction.isChecked())
        # settings.setValue("autoRecalc", autoRecalcAction.isChecked())
        pass


    def okToContinue(self):
        pass
        #
        # if (isWindowModified())
        #     int r = QMessageBox.warning(self, tr("Spreadsheet"),
        #                     tr("The document has been modified.\n"
        #                        "Do you want to save your changes?"),
        #                     QMessageBox.Yes | QMessageBox.No
        #                     | QMessageBox.Cancel)
        #     if (r == QMessageBox.Yes)
        #         return save()
        #      else if (r == QMessageBox.Cancel)
        #         return false
        #
        #
        # return true
        #

    # def loadFile(const QString &fileName)
    def loadFile(self,fileName):

        pass
        # if (!spreadsheet.readFile(fileName))
        #     statusBar().showMessage(tr("Loading canceled"), 2000)
        #     return false
        #
        #
        # setCurrentFile(fileName)
        # statusBar().showMessage(tr("File loaded"), 2000)
        # return true
        #

    # def saveFile(const QString &fileName)
    def saveFile(self,fileName):
        #
        # if (!spreadsheet.writeFile(fileName))
        #     statusBar().showMessage(tr("Saving canceled"), 2000)
        #     return false
        #
        #
        # setCurrentFile(fileName)
        # statusBar().showMessage(tr("File saved"), 2000)
        # return true
        pass


    # def setCurrentFile(const QString &fileName)
    def setCurrentFile(self,fileName):
        pass
        # curFile = fileName
        # setWindowModified(false)
        #
        # QString shownName = tr("Untitled")
        # if (!curFile.isEmpty())
        #     shownName = strippedName(curFile)
        #     recentFiles.removeAll(curFile)
        #     recentFiles.prepend(curFile)
        #     updateRecentFileActions()
        #
        #
        # setWindowTitle(tr("%1[*] - %2").arg(shownName)
        #                                .arg(tr("Spreadsheet")))
        #

    def updateRecentFileActions(self):
        pass
        # QMutableStringListIterator i(recentFiles)
        # while (i.hasNext())
        #     if (!QFile.exists(i.next()))
        #         i.remove()
        #
        #
        # for (int j = 0 j < MaxRecentFiles ++j)
        #     if (j < recentFiles.count())
        #         QString text = tr("&%1 %2")
        #                        .arg(j + 1)
        #                        .arg(strippedName(recentFiles[j]))
        #         recentFileActions[j].setText(text)
        #         recentFileActions[j].setData(recentFiles[j])
        #         recentFileActions[j].setVisible(true)
        #      else
        #         recentFileActions[j].setVisible(false)
        #
        #
        # separatorAction.setVisible(!recentFiles.isEmpty())
        #

    # def strippedName(const QString &fullFileName)
    def strippedName(self,fullFileName):
        pass
        # return QFileInfo(fullFileName).fileName()

if __name__ == "__main__":
    from  PyQt4.QtGui import QApplication
    import sys
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()

    app.exec_()
