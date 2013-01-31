#!usr/bin/env python
"""

        """

import sys

from PySide import QtGui

from ui.mainwindow import MainWindow
from db.local import LocalDatabase


if __name__ == '__main__':

    localdb = LocalDatabase()
    localdb.create_database()

    app = QtGui.QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()