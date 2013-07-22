#!/usr/bin/env python

# server.py - DBus server application
# Copyright (C) 2013  Sören Brinkmann <soeren.brinkmann@gmail.com>
# Based on the example from:
#   http://www.documentroot.net/en/linux/python-dbus-tutorial
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

from PyQt4.QtCore import *
import dbus
import dbus.service
from dbus.mainloop.qt import DBusQtMainLoop
 
class Mdt(dbus.service.Object):
  def __init__(self):
    busName = dbus.service.BusName('my.dbus.test.srv', bus = dbus.SessionBus())
    dbus.service.Object.__init__(self, busName, '/MDT')
 
  @dbus.service.method('my.dbus.test',)
  def hello(self): print("Hello world!")
 
DBusQtMainLoop(set_as_default = True)
app = QCoreApplication([])
mdt = Mdt()
app.exec_()
