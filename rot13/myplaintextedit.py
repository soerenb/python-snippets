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

from PyQt4 import QtCore, QtGui
import rot13

class myPlainTextEdit(QtGui.QPlainTextEdit):
    @QtCore.pyqtSlot()
    def decryptText(self):
        ct = rot13.encr(self.toPlainText())
        self.setPlainText("".join(ct))
