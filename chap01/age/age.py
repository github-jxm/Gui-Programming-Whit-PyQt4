#!/usr/bin/env python
#coding=utf-8

from PyQt4.QtCore import Qt, QObject, SIGNAL, SLOT
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QWidget, QSpinBox, QSlider, QHBoxLayout
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Enter Your Age")

    spinBox = QSpinBox()
    slider = QSlider(Qt.Horizontal)
    spinBox.setRange(0, 130)
    slider.setRange(0, 130)

    QObject.connect(spinBox, SIGNAL("valueChanged(int)"),
                     slider, SLOT("setValue(int)"))

    QObject.connect(slider, SIGNAL("valueChanged(int)"),
                     spinBox, SLOT("setValue(int)"))

    spinBox.setValue(35)

    layout = QHBoxLayout()    # 水平布局
    layout.addWidget(spinBox) # 添加 水平 布局
    layout.addWidget(slider)  # 添加 水平 布局

    window.setLayout(layout)

    window.show()

    app.exec_()
