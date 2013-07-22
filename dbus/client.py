#!/usr/bin/env python

# client.py - DBus client application
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

import dbus
import sys

bus = dbus.SessionBus()

try:
    server = bus.get_object('my.dbus.test.srv', '/MDT')
except dbus.exceptions.DBusException as msg:
    print(msg)
    sys.exit(1)

try:
    server.hello(dbus_interface="my.dbus.test")
except dbus.exceptions.DBusException as msg:
    print(msg)
    sys.exit(1)
