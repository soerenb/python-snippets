#!/usr/bin/env python

# server.py - UNIX Domain Socket server example
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

import socket
import os
import sys

SOCKET_FILE = "./sock_srv"

try:
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
except OSError as msg:
    print(msg)
    sys.exit(1)

try:
    s.bind(SOCKET_FILE)
except OSError as msg:
    print(msg)
    s.close()
    sys.exit(1)

try:
    s.listen(5)
    con, addr = s.accept()
except OSError as msg:
    print(msg)
    s.close()
    os.unlink(SOCKET_FILE)
    sys.exit(1)

while True:
    try:
        msg = con.recv(1024)
    except OSError as msg:
        print(msg)
        break
    print("SERVER: received {} bytes".format(len(msg)))

    try:
        n = con.send(msg)
    except OSError as msg:
        print(msg)
        break
    print("SERVER: sent {} bytes".format(n))

con.close()
s.close()
os.unlink(SOCKET_FILE)
