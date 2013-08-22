# mypopup.py - Wrapper class for popup message boxes
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
import popup

class myPopup(QtGui.QDialog):
    def __init__(self, parent = None):
        super(myPopup, self).__init__(parent)
        self.ui = popup.Ui_popup()
        self.ui.setupUi(self)
