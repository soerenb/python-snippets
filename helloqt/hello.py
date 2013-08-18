#!/usr/bin/env python

import sys
import hello_gui
from PyQt4 import QtCore, QtGui, Qt

def sayHello():
    print("world")

def label_hello():
    ui.label.setText("world!!")

app = QtGui.QApplication(sys.argv)
window = QtGui.QDialog()
ui = hello_gui.Ui_Dialog()
ui.setupUi(window)
window.show()

# connect button events to functions
app.connect(ui.pushButton, Qt.SIGNAL("clicked()"), sayHello)
app.connect(ui.pushButton, Qt.SIGNAL("pressed()"), label_hello)

sys.exit(app.exec_())
