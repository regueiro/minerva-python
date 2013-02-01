#!usr/bin/env python

"""
Minerva - An artwork manager for the XBMC Media Center

Launches the Qt interface

"""

import sys

from PySide import QtGui

from ui.mainwindow import MainWindow


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()