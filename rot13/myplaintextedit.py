# myplaintextedit.py - pyqt plainTextEdit derived class
# Copyright (C) 2013  Sören Brinkmann <soeren.brinkmann@gmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from PyQt4 import QtCore, QtGui, Qt
import rot13

class myPlainTextEdit(QtGui.QPlainTextEdit):
    def __init__(self, qwidget):
        self.cypher = 0
        super(myPlainTextEdit, self).__init__(qwidget)

    @QtCore.pyqtSlot()
    def decryptText(self):
        ct = rot13.encr(self.toPlainText(), self.cypher)
        self.setPlainText("".join(ct))

    @QtCore.pyqtSlot(bool)
    def setCypher(self, rot13):
        if rot13 == True:
            self.cypher = 0
        else:
            self.cypher = 1

    @QtCore.pyqtSlot()
    def loadFile(self):
        path = QtGui.QFileDialog.getOpenFileName(self)
        if not path:
            return

        try:
            fin = open(path, "r")
        except IOError:
            print("unable to open '{}'".format(path))
            return

        pt = fin.read()
        fin.close()

        self.setPlainText("".join(pt))
