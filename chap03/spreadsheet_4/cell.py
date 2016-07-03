#!/usr/bin/env python
#coding=utf-8
from copy import deepcopy
from PyQt4.QtCore import QObject, QVariant, Qt, QString, QChar
from PyQt4.QtGui import QTableWidgetItem


class Cell(QObject):
    def __init__(self):
        super(Cell, self).__init__()
        self.value = QVariant()
        self.cacheIsDirty=False
        self.cachedValue =  QVariant()
        self.setDirty()
    def clone(self):
       return deepcopy(self)

    def setData(self,role,value):
        QTableWidgetItem.setData(role,value)
        if(role == Qt.EditRole):
            self.setDirty()

    def data(self,role):
        if role == Qt.DisplayRole :
            if self.value.isValid():
                return self.value.toString()
            else:
                return "####"

        elif (role == Qt.TextAlignmentRole):
            if (self.value.type() == QVariant.String):
                return int(Qt.AlignLeft | Qt.AlignVCenter)
            else:
                return int(Qt.AlignRight | Qt.AlignVCenter)
        else:
            return QTableWidgetItem.data(role)

    # def setFormula(self, &formula):
    def setFormula(self, formula):
        self.setData(Qt.EditRole, formula)

    def formula(self) :
        return self.data(Qt.EditRole).toString()


    def setDirty(self):
        self.cacheIsDirty = True


    def value(self) :

        if (self.cacheIsDirty):
            self.cacheIsDirty = False

            formulaStr = self.formula()
            if (formulaStr.startsWith('\'')):
                self.cachedValue = formulaStr.mid(1)
            elif (formulaStr.startsWith('=')):
                self.cachedValue = self.Invalid
                expr = QString(formulaStr.mid(1))
                expr.replace(" ", "")
                expr.append(QChar.Null)

                pos = int(0)
                cachedValue = self.evalExpression(expr, pos)
                if (expr[pos] != QChar.Null):
                    cachedValue = self.Invalid
            else:
                pass
                ok = bool(False)
                # double d = formulaStr.toDouble(&ok)
                # if (ok)
                #     cachedValue = d
                #  else
                #     cachedValue = formulaStr
                #


        return self.cachedValue


    # def evalExpression(const QString &str, int &pos) const
    def evalExpression(self,str, pos):

        result = QVariant(self.evalTerm(str, pos))
        # while (str[pos] != QChar.Null):
        #     op = QChar(str[pos])
        #     if (op != '+' && op != '-'):
        #         return result
        #     pos = pos + 1
        #
        #     term = QVariant(self.evalTerm(str, pos))
        #     if (result.type() == QVariant.Double
        #             && term.type() == QVariant.Double)
        #         if (op == '+')
        #             result = result.toDouble() + term.toDouble()
        #          else
        #             result = result.toDouble() - term.toDouble()
        #
        #      else
        #         result = Invalid


        return QVariant(result)


    # QVariant Cell.evalTerm(const QString &str, int &pos) const
    def evalTerm(self,str, pos) :
        pass
        #
        # QVariant result = evalFactor(str, pos)
        # while (str[pos] != QChar.Null)
        #     QChar op = str[pos]
        #     if (op != '*' && op != '/')
        #         return result
        #     ++pos
        #
        #     QVariant factor = evalFactor(str, pos)
        #     if (result.type() == QVariant.Double
        #             && factor.type() == QVariant.Double)
        #         if (op == '*')
        #             result = result.toDouble() * factor.toDouble()
        #          else
        #             if (factor.toDouble() == 0.0)
        #                 result = Invalid
        #              else
        #                 result = result.toDouble() / factor.toDouble()
        #
        #
        #      else
        #         result = Invalid
        #

        # return result
        return QVariant(0)

    # QVariant Cell.evalFactor(const QString &str, int &pos) const
    def evalFactor(self,str, pos) :
        #
        # QVariant result
        # bool negative = false
        #
        # if (str[pos] == '-')
        #     negative = true
        #     ++pos
        #
        #
        # if (str[pos] == '(')
        #     ++pos
        #     result = evalExpression(str, pos)
        #     if (str[pos] != ')')
        #         result = Invalid
        #     ++pos
        #  else
        #     QRegExp regExp("[A-Za-z][1-9][0-9]0,2")
        #     QString token
        #
        #     while (str[pos].isLetterOrNumber() || str[pos] == '.')
        #         token += str[pos]
        #         ++pos
        #
        #
        #     if (regExp.exactMatch(token))
        #         int column = token[0].toUpper().unicode() - 'A'
        #         int row = token.mid(1).toInt() - 1
        #
        #         Cell *c = static_cast<Cell *>(
        #                           tableWidget()->item(row, column))
        #         if (c)
        #             result = c->value()
        #          else
        #             result = 0.0
        #
        #      else
        #         bool ok
        #         result = token.toDouble(&ok)
        #         if (!ok)
        #             result = Invalid
        #
        #
        #
        # if (negative)
        #     if (result.type() == QVariant.Double)
        #         result = -result.toDouble()
        #      else
        #         result = Invalid
        #
        #
        # return result

        return QVariant(0)

#
# QTableWidgetItem *Cell.clone() const
#
#     return new Cell(*this)
#
#
# void Cell.setData(int role, const QVariant &value)
#
#     QTableWidgetItem.setData(role, value)
#     if (role == Qt.EditRole)
#         setDirty()
#
#
# QVariant Cell.data(int role) const
#
#     if (role == Qt.DisplayRole)
#         if (value().isValid())
#             return value().toString()
#          else
#             return "####"
#
#      else if (role == Qt.TextAlignmentRole)
#         if (value().type() == QVariant.String)
#             return int(Qt.AlignLeft | Qt.AlignVCenter)
#          else
#             return int(Qt.AlignRight | Qt.AlignVCenter)
#
#      else
#         return QTableWidgetItem.data(role)
#
#
#
# void Cell.setFormula(const QString &formula)
#
#     setData(Qt.EditRole, formula)


# QString Cell.formula() const
#
#     return data(Qt.EditRole).toString()

#
# void Cell.setDirty()
#
#     cacheIsDirty = true


# const QVariant Invalid
#
# QVariant Cell.value() const
#
#     if (cacheIsDirty)
#         cacheIsDirty = false
#
#         QString formulaStr = formula()
#         if (formulaStr.startsWith('\''))
#             cachedValue = formulaStr.mid(1)
#          else if (formulaStr.startsWith('='))
#             cachedValue = Invalid
#             QString expr = formulaStr.mid(1)
#             expr.replace(" ", "")
#             expr.append(QChar.Null)
#
#             int pos = 0
#             cachedValue = evalExpression(expr, pos)
#             if (expr[pos] != QChar.Null)
#                 cachedValue = Invalid
#          else
#             bool ok
#             double d = formulaStr.toDouble(&ok)
#             if (ok)
#                 cachedValue = d
#              else
#                 cachedValue = formulaStr
#
#
#
#     return cachedValue
#
#
# QVariant Cell.evalExpression(const QString &str, int &pos) const
#
#     QVariant result = evalTerm(str, pos)
#     while (str[pos] != QChar.Null)
#         QChar op = str[pos]
#         if (op != '+' && op != '-')
#             return result
#         ++pos
#
#         QVariant term = evalTerm(str, pos)
#         if (result.type() == QVariant.Double
#                 && term.type() == QVariant.Double)
#             if (op == '+')
#                 result = result.toDouble() + term.toDouble()
#              else
#                 result = result.toDouble() - term.toDouble()
#
#          else
#             result = Invalid
#
#
#     return result
#
#
# QVariant Cell.evalTerm(const QString &str, int &pos) const
#
#     QVariant result = evalFactor(str, pos)
#     while (str[pos] != QChar.Null)
#         QChar op = str[pos]
#         if (op != '*' && op != '/')
#             return result
#         ++pos
#
#         QVariant factor = evalFactor(str, pos)
#         if (result.type() == QVariant.Double
#                 && factor.type() == QVariant.Double)
#             if (op == '*')
#                 result = result.toDouble() * factor.toDouble()
#              else
#                 if (factor.toDouble() == 0.0)
#                     result = Invalid
#                  else
#                     result = result.toDouble() / factor.toDouble()
#
#
#          else
#             result = Invalid
#
#
#     return result
#
#
# QVariant Cell.evalFactor(const QString &str, int &pos) const
#
#     QVariant result
#     bool negative = false
#
#     if (str[pos] == '-')
#         negative = true
#         ++pos
#
#
#     if (str[pos] == '(')
#         ++pos
#         result = evalExpression(str, pos)
#         if (str[pos] != ')')
#             result = Invalid
#         ++pos
#      else
#         QRegExp regExp("[A-Za-z][1-9][0-9]0,2")
#         QString token
#
#         while (str[pos].isLetterOrNumber() || str[pos] == '.')
#             token += str[pos]
#             ++pos
#
#
#         if (regExp.exactMatch(token))
#             int column = token[0].toUpper().unicode() - 'A'
#             int row = token.mid(1).toInt() - 1
#
#             Cell *c = static_cast<Cell *>(
#                               tableWidget()->item(row, column))
#             if (c)
#                 result = c->value()
#              else
#                 result = 0.0
#
#          else
#             bool ok
#             result = token.toDouble(&ok)
#             if (!ok)
#                 result = Invalid
#
#
#
#     if (negative)
#         if (result.type() == QVariant.Double)
#             result = -result.toDouble()
#          else
#             result = Invalid
#
#
#     return result

