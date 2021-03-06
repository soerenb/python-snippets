#!/usr/bin/env python

# rot13_gui.py - Rot13 Qt GUI
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

import sys
import rot13_gui
from PyQt4 import QtCore, QtGui, Qt

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
ui = rot13_gui.Ui_MainWindow()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())
