#!/usr/bin/env python
#coding=utf8

#include "cell.h"
#include "spreadsheet.h"
from PyQt4.QtCore import QChar, QString, pyqtSlot
from PyQt4.QtGui import QWidget,QTableWidget
# from cell import Cell

class Spreadsheet(QTableWidget):
    def __init__(self,parent=None):
        super(Spreadsheet, self).__init__(parent)

        # 临时
        self.setRowCount(10)
        self.setColumnCount(5)

        self.autoRecalc = True
        #
        # setItemPrototype(new Cell);
        # setSelectionMode(ContiguousSelection);
        #
        # connect(this, SIGNAL(itemChanged(QTableWidgetItem *)),
        #         this, SLOT(somethingChanged()));
        #
        # clear();


    def currentLocation(self):
        return QChar('A' + self.currentColumn()) + \
               QString.number(self.currentRow() + 1)

    def currentFormula(self):
        return self.formula(self.currentRow(), self.currentColumn());

    # QTableWidgetSelectionRange Spreadsheet::selectedRange() const
    def selectedRange(self):
        # QList<QTableWidgetSelectionRange> ranges = selectedRanges();
        ranges = self.selectedRanges()
        if (ranges.isEmpty()):
            return self.QTableWidgetSelectionRange()
        return ranges.first();

    def clear(self):
        self.setRowCount(0);
        self.setColumnCount(0);
        # self.setRowCount(RowCount);
        # self.setColumnCount(ColumnCount);

        # for (int i = 0; i < ColumnCount; ++i) {
        #     QTableWidgetItem *item = new QTableWidgetItem;
        #     item->setText(QString(QChar('A' + i)));
        #     setHorizontalHeaderItem(i, item);
        # }

        self.setCurrentCell(0, 0);

    # bool Spreadsheet::readFile(const QString &fileName)
    def readFile(self,fileName):
        # QFile file(fileName);
        # if (!file.open(QIODevice::ReadOnly)) {
        #     QMessageBox::warning(this, tr("Spreadsheet"),
        #                          tr("Cannot read file %1:\n%2.")
        #                          .arg(file.fileName())
        #                          .arg(file.errorString()));
        #     return false;
        # }
        #
        # QDataStream in(&file);
        # in.setVersion(QDataStream::Qt_4_3);
        #
        # quint32 magic;
        # in >> magic;
        # if (magic != MagicNumber) {
        #     QMessageBox::warning(this, tr("Spreadsheet"),
        #                          tr("The file is not a Spreadsheet file."));
        #     return false;
        # }
        #
        # clear();
        #
        # quint16 row;
        # quint16 column;
        # QString str;
        #
        # QApplication::setOverrideCursor(Qt::WaitCursor);
        # while (!in.atEnd()) {
        #     in >> row >> column >> str;
        #     setFormula(row, column, str);
        # }
        # QApplication::restoreOverrideCursor();
        return True

    # bool Spreadsheet::writeFile(const QString &fileName)
    def writeFile(self,fileName):
        # QFile file(fileName);
        # if (!file.open(QIODevice::WriteOnly)) {
        #     QMessageBox::warning(this, tr("Spreadsheet"),
        #                          tr("Cannot write file %1:\n%2.")
        #                          .arg(file.fileName())
        #                          .arg(file.errorString()));
        #     return false;
        # }
        #
        # QDataStream out(&file);
        # out.setVersion(QDataStream::Qt_4_3);
        #
        # out << quint32(MagicNumber);
        #
        # QApplication::setOverrideCursor(Qt::WaitCursor);
        # for (int row = 0; row < RowCount; ++row) {
        #     for (int column = 0; column < ColumnCount; ++column) {
        #         QString str = formula(row, column);
        #         if (!str.isEmpty())
        #             out << quint16(row) << quint16(column) << str;
        #     }
        # }
        # QApplication::restoreOverrideCursor();
        return True

    # void Spreadsheet::sort(const SpreadsheetCompare &compare)
    def sort(self,compare):
        # QList<QStringList> rows;
        # QTableWidgetSelectionRange range = selectedRange();
        # int i;
        #
        # for (i = 0; i < range.rowCount(); ++i) {
        #     QStringList row;
        #     for (int j = 0; j < range.columnCount(); ++j)
        #         row.append(formula(range.topRow() + i,
        #                            range.leftColumn() + j));
        #     rows.append(row);
        # }
        #
        # qStableSort(rows.begin(), rows.end(), compare);
        #
        # for (i = 0; i < range.rowCount(); ++i) {
        #     for (int j = 0; j < range.columnCount(); ++j)
        #         setFormula(range.topRow() + i, range.leftColumn() + j,
        #                    rows[i][j]);
        # }
        #
        # clearSelection();
        # somethingChanged();
        pass

    @pyqtSlot()
    def cut(self):
        # copy();
        # __del();
        pass

    @pyqtSlot()
    def copy(self):
        # QTableWidgetSelectionRange range = selectedRange();
        # QString str;
        #
        # for (int i = 0; i < range.rowCount(); ++i) {
        #     if (i > 0)
        #         str += "\n";
        #     for (int j = 0; j < range.columnCount(); ++j) {
        #         if (j > 0)
        #             str += "\t";
        #         str += formula(range.topRow() + i, range.leftColumn() + j);
        #     }
        # }
        # QApplication::clipboard()->setText(str);
        pass

    @pyqtSlot()
    def paste(self):
    #     QTableWidgetSelectionRange range = selectedRange();
    #     QString str = QApplication::clipboard()->text();
    #     QStringList rows = str.split('\n');
    #     int numRows = rows.count();
    #     int numColumns = rows.first().count('\t') + 1;
    #
    #     if (range.rowCount() * range.columnCount() != 1
    #             && (range.rowCount() != numRows
    #                 || range.columnCount() != numColumns)) {
    #         QMessageBox::information(this, tr("Spreadsheet"),
    #                 tr("The information cannot be pasted because the copy "
    #                    "and paste areas aren't the same size."));
    #         return;
    #     }
    #
    #     for (int i = 0; i < numRows; ++i) {
    #         QStringList columns = rows[i].split('\t');
    #         for (int j = 0; j < numColumns; ++j) {
    #             int row = range.topRow() + i;
    #             int column = range.leftColumn() + j;
    #             if (row < RowCount && column < ColumnCount)
    #                 setFormula(row, column, columns[j]);
    #         }
    #     }
    #     somethingChanged();
    # }
        pass

    def __del(self):
        pass
        # QList<QTableWidgetItem *> items = selectedItems();
        # if (!items.isEmpty()) {
        #     foreach (QTableWidgetItem *item, items)
        #         delete item;
        #     somethingChanged();
        # }

    @pyqtSlot()
    def selectCurrentRow(self):
        pass
        # selectRow(currentRow());

    @pyqtSlot()
    def selectCurrentColumn(self):
        pass
        # selectColumn(currentColumn());

    # void Spreadsheet::recalculate()
    def recalculate(self):
        # for (int row = 0; row < RowCount; ++row) {
        #     for (int column = 0; column < ColumnCount; ++column) {
        #         if (cell(row, column))
        #             cell(row, column)->setDirty();
        #     }
        # }
        # viewport()->update();
        pass

    @pyqtSlot()
    def setAutoRecalculate(recalc):
        # autoRecalc = recalc;
        # if (autoRecalc)
        #     recalculate();
        pass

    # void Spreadsheet::findNext(const QString &str, Qt::CaseSensitivity cs)
    def findNext(self,str, cs):
    #     int row = currentRow();
    #     int column = currentColumn() + 1;
    #
    #     while (row < RowCount) {
    #         while (column < ColumnCount) {
    #             if (text(row, column).contains(str, cs)) {
    #                 clearSelection();
    #                 setCurrentCell(row, column);
    #                 activateWindow();
    #                 return;
    #             }
    #             ++column;
    #         }
    #         column = 0;
    #         ++row;
    #     }
    #     QApplication::beep();
        pass

    # void Spreadsheet::findPrevious(const QString &str,
    #                                      Qt::CaseSensitivity cs)
    def findPrevious(self, str, cs):
        # int row = currentRow();
        # int column = currentColumn() - 1;
        #
        # while (row >= 0) {
        #     while (column >= 0) {
        #         if (text(row, column).contains(str, cs)) {
        #             clearSelection();
        #             setCurrentCell(row, column);
        #             activateWindow();
        #             return;
        #         }
        #         --column;
        #     }
        #     column = ColumnCount - 1;
        #     --row;
        # QApplication::beep();
        pass

    def somethingChanged(self):
        # if (autoRecalc)
        #     recalculate();
        # emit modified();
        pass

    # Cell *Spreadsheet::cell(int row, int column) const
    def cell(self, row,  column):
        # return static_cast<Cell *>(item(row, column));
        return self.item(row, column)

    # void Spreadsheet::setFormula(int row, int column,
    #                                           const QString &formula)
    def setFormula(self,row, column, formula):
        # Cell *c = cell(row, column);
        # if (!c) {
        #     c = new Cell;
        #     setItem(row, column, c);
        # }
        # c->setFormula(formula);
        pass

    def formula(self,row, column):
        # Cell *c = cell(row, column);
        # if (c) {
        #     return c->formula();
        # } else {
        #     return "";
        # }
        pass

    def text(self,row,column):
        # Cell *c = cell(row, column);
        # if (c) {
        #     return c->text();
        # } else {
        #     return "";
        # }
        pass

    # bool SpreadsheetCompare::operator()(const QStringList &row1,
    # #                                           const QStringList &row2) const
    # bool SpreadsheetCompare::operator()(const QStringList &row1,
    #                                     const QStringList &row2) const
    # {
    #     for (int i = 0; i < KeyCount; ++i) {
    #         int column = keys[i];
    #         if (column != -1) {
    #             if (row1[column] != row2[column]) {
    #                 if (ascending[i]) {
    #                     return row1[column] < row2[column];
    #                 } else {
    #                     return row1[column] > row2[column];
    #                 }
    #             }
    #         }
    #     }
    #     return false;
    # }


if __name__ == "__main__":
    from PyQt4.QtGui import QApplication
    import sys
    app = QApplication(sys.argv)
    sheet = Spreadsheet()
    sheet.show()
    app.exec_()

