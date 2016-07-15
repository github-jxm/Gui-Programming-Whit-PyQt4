#!/usr/bin/env python
# coding=utf-8

from PyQt4.QtCore import SIGNAL, SLOT, pyqtSlot, Qt
from PyQt4.QtGui import QMainWindow, QIcon, QAction, QKeySequence, QMessageBox
from spreadsheet import Spreadsheet

import spreadsheet_rc


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowIcon(QIcon(":/images/icon.png"))
        self.setCurrentFile("")

        # ----------- 数据 -------------
        self.spreadsheet = Spreadsheet()
        self.setCentralWidget(self.spreadsheet)

        self.findDialog = None
        self.locationLabel = None
        self.formulaLabel = None
        self.recentFiles = None  # QStringList recentFiles;
        self.curFile = None      # QString curFile;

        self.MaxRecentFiles = 5
        self.recentFileActions = [None] * self.MaxRecentFiles
        #
        self.separatorAction = None
        # #
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
        # self.qApp = QApplication([]) # 这样写 有问题


        self.createActions()
        self.createMenus()
        self.createContextMenu()
        self.createToolBars()
        self.createStatusBar()

        # self.readSettings()

    # def closeEvent(self, event):
    #     if (self.okToContinue()):
    #         self.writeSettings()
    #         event.accept()
    #     else:
    #         event.ignore()

    @pyqtSlot()
    def newFile(self):
        if (self.okToContinue()):
            pass
            # spreadsheet.clear()
            # setCurrentFile("")

    @pyqtSlot()
    def open(self):
        pass

    @pyqtSlot()
    def save(self):
        pass

    @pyqtSlot()
    def saveAs(self):
        pass

    @pyqtSlot()
    def find(self):
        pass

    @pyqtSlot()
    def goToCell(self):
        pass

    @pyqtSlot()
    def sort(self):
        pass

    # 关于
    @pyqtSlot()
    def about(self):
        QMessageBox.about(self, str("About Spreadsheet"),
                str("<h2>Spreadsheet 1.1</h2>"
                   "<p>Copyright &copy 2008 Software Inc."
                   "<p>Spreadsheet is a small application that "
                   "demonstrates QAction, QMainWindow, QMenuBar, "
                   "QStatusBar, QTableWidget, QToolBar, and many other "
                   "Qt classes."))

    @pyqtSlot()
    def openRecentFile(self):
        pass

    @pyqtSlot()
    def updateStatusBar(self):
        pass

    def spreadsheetModified(self):
        pass

    # 创建 Actions
    def createActions(self):

        # 新建
        self.newAction = QAction(str("&New"), self)
        self.newAction.setIcon(QIcon(":/images/new.png"))
        self.newAction.setShortcut(QKeySequence.New)
        self.newAction.setStatusTip(str("Create a new spreadsheet file"))
        self.connect(self.newAction, SIGNAL("triggered()"), self, SLOT("newFile()"))

        # 打开
        self.openAction = QAction(str("&Open..."), self)
        self.openAction.setIcon(QIcon(":/images/open.png"))
        self.openAction.setShortcut(QKeySequence.Open)
        self.openAction.setStatusTip(str("Open an existing spreadsheet file"))
        self.connect(self.openAction, SIGNAL("triggered()"), self, SLOT("open()"))

        # 保存
        self.saveAction = QAction(str("&Save"), self)
        self.saveAction.setIcon(QIcon(":/images/save.png"))
        self.saveAction.setShortcut(QKeySequence.Save)
        self.saveAction.setStatusTip(str("Save the spreadsheet to disk"))
        self.connect(self.saveAction, SIGNAL("triggered()"), self, SLOT("save()"))

        # 另存为
        self.saveAsAction = QAction(str("Save &As..."), self)
        self.saveAsAction.setStatusTip(str("Save the spreadsheet under a name"))
        self.connect(self.saveAsAction, SIGNAL("triggered()"), self, SLOT("saveAs()"))

        for i in range(self.MaxRecentFiles):
            self.recentFileActions[i] = QAction(self)
            self.recentFileActions[i].setVisible(False)
            self.connect(self.recentFileActions[i], SIGNAL("triggered()"),
                         self, SLOT("openRecentFile()"))
        # 退出
        self.exitAction = QAction(str("E&xit"), self)
        self.exitAction.setShortcut(str("Ctrl+Q"))
        self.exitAction.setStatusTip(str("Exit the application"))
        self.connect(self.exitAction, SIGNAL("triggered()"), self, SLOT("close()"))

        # -------------

        # 剪切
        self.cutAction = QAction(str("Cu&t"), self)
        self.cutAction.setIcon(QIcon(":/images/cut.png"))
        self.cutAction.setShortcut(QKeySequence.Cut)
        self.cutAction.setStatusTip(str("Cut the current selection's contents "
                                        "to the clipboard"))
        self.connect(self.cutAction, SIGNAL("triggered()"), self.spreadsheet, SLOT("cut()"))

        # 拷贝
        self.copyAction = QAction(str("&Copy"), self)
        self.copyAction.setIcon(QIcon(":/images/copy.png"))
        self.copyAction.setShortcut(QKeySequence.Copy)
        self.copyAction.setStatusTip(str("Copy the current selection's contents "
                                         "to the clipboard"))
        self.connect(self.copyAction, SIGNAL("triggered()"), self.spreadsheet, SLOT("copy()"))

        # 黏贴
        self.pasteAction = QAction(str("&Paste"), self)
        self.pasteAction.setIcon(QIcon(":/images/paste.png"))
        self.pasteAction.setShortcut(QKeySequence.Paste)
        self.pasteAction.setStatusTip(str("Paste the clipboard's contents into "
                                          "the current selection"))
        self.connect(self.pasteAction, SIGNAL("triggered()"),
                self.spreadsheet, SLOT("paste()"))

        self.deleteAction = QAction(str("&Delete"), self)
        self.deleteAction.setShortcut(QKeySequence.Delete)
        self.deleteAction.setStatusTip(str("Delete the current selection's "
                                           "contents"))
        # self.connect(self.deleteAction, SIGNAL("triggered()"),
        #         self.spreadsheet, SLOT(del()))

        self.selectRowAction = QAction(str("&Row"), self)
        self.selectRowAction.setStatusTip(str("Select all the cells in the "
                                              "current row"))
        self.connect(self.selectRowAction, SIGNAL("triggered()"),
                self.spreadsheet, SLOT("selectCurrentRow()"))

        self.selectColumnAction = QAction(str("&Column"), self)
        self.selectColumnAction.setStatusTip(str("Select all the cells in the "
                                                 "current column"))
        self.connect(self.selectColumnAction, SIGNAL("triggered()"),
                self.spreadsheet, SLOT("selectCurrentColumn()"))

        self.selectAllAction = QAction(str("&All"), self)
        self.selectAllAction.setShortcut(QKeySequence.SelectAll)
        self.selectAllAction.setStatusTip(str("Select all the cells in the "
                                              "spreadsheet"))
        self.connect(self.selectAllAction, SIGNAL("triggered()"),
                self.spreadsheet, SLOT("selectAll()"))

        self.findAction = QAction(str("&Find..."), self)
        self.findAction.setIcon(QIcon(":/images/find.png"))
        self.findAction.setShortcut(QKeySequence.Find)
        self.findAction.setStatusTip(str("Find a matching cell"))
        self.connect(self.findAction, SIGNAL("triggered()"), self, SLOT("find()"))

        self.goToCellAction = QAction(str("&Go to Cell..."), self)
        self.goToCellAction.setIcon(QIcon(":/images/gotocell.png"))
        self.goToCellAction.setShortcut(str("Ctrl+G"))
        self.goToCellAction.setStatusTip(str("Go to the specified cell"))
        self.connect(self.goToCellAction, SIGNAL("triggered()"),
                self, SLOT("goToCell()"))

        self.recalculateAction = QAction(str("&Recalculate"), self)
        self.recalculateAction.setShortcut(str("F9"))
        self.recalculateAction.setStatusTip(str("Recalculate all the "
                                                "spreadsheet's formulas"))
        self.connect(self.recalculateAction, SIGNAL("triggered()"),
                self.spreadsheet, SLOT("recalculate()"))

        self.sortAction = QAction(str("&Sort..."), self)
        self.sortAction.setStatusTip(str("Sort the selected cells or all the "
                                         "cells"))
        self.connect(self.sortAction, SIGNAL("triggered()"), self, SLOT("sort()"))

        self.showGridAction = QAction(str("&Show Grid"), self)
        self.showGridAction.setCheckable(True)
        self.showGridAction.setChecked(self.spreadsheet.showGrid())
        self.showGridAction.setStatusTip(str("Show or hide the spreadsheet's "
                                             "grid"))
        self.connect(self.showGridAction, SIGNAL("toggled(bool)"),
                self.spreadsheet, SLOT("setShowGrid(bool)"))

        self.autoRecalcAction = QAction(str("&Auto-Recalculate"), self)
        self.autoRecalcAction.setCheckable(True)
        # self.autoRecalcAction.setChecked(self.spreadsheet.autoRecalculate())
        self.autoRecalcAction.setStatusTip(str("Switch auto-recalculation on or "
                                               "off"))
        # self.connect(self.autoRecalcAction, SIGNAL("toggled(bool)"),\
                   # self.spreadsheet, SLOT("setAutoRecalculate(bool)"))

        self.aboutAction = QAction(str("&About"), self)
        self.aboutAction.setStatusTip(str("Show the application's About box"))
        self.connect(self.aboutAction, SIGNAL("triggered()"), self, SLOT("about()"))

        self.aboutQtAction = QAction(str("About &Qt"), self)
        self.aboutQtAction.setStatusTip(str("Show the Qt library's About box"))
        # self.connect(self.aboutQtAction, SIGNAL("triggered()"), self.qApp, SLOT("aboutQt()"))

    # 创建 菜单栏
    def createMenus(self):

        self.fileMenu = self.menuBar().addMenu(str("&File"))
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.saveAsAction)
        self.separatorAction = self.fileMenu.addSeparator()

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

    # 添加 上下文菜单,右键快捷菜单
    def createContextMenu(self):
        pass
        self.spreadsheet.addAction(self.cutAction)
        self.spreadsheet.addAction(self.copyAction)
        self.spreadsheet.addAction(self.pasteAction)
        self.spreadsheet.setContextMenuPolicy(Qt.ActionsContextMenu)

    def createToolBars(self):
        pass

    def createStatusBar(self):
        pass

    def readSettings(self):
        pass

    def writeSettings(self):
        pass

    def okToContinue(self):
        pass

    # def loadFile(const QString &fileName)
    def loadFile(self, fileName):
        pass

    # def saveFile(const QString &fileName)
    def saveFile(self, fileName):
        pass

    # def setCurrentFile(const QString &fileName)
    def setCurrentFile(self, fileName):
        pass

    def updateRecentFileActions(self):
        pass

    # def strippedName(const QString &fullFileName)
    def strippedName(self, fullFileName):
        pass
        # return QFileInfo(fullFileName).fileName()


if __name__ == "__main__":
    from  PyQt4.QtGui import QApplication
    import sys

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()
