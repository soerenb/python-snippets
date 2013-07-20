#!/usr/bin/env python

# client.py - UNIX Domain Socket client example
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
import sys

try:
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
except OSError as msg:
    print(msg)
    sys.exit(1)

try:
    s.connect("./sock_srv")
except OSError as msg:
    print(msg)
    s.close()
    sys.exit(1)

while True:
    msg = input("Enter message to transmit: ")
    if (msg.lower() == "quit") or (msg.lower() == "exit"):
        break

    try:
        n = s.send(msg.encode())
    except OSError as msg:
        print(msg)
        break;
    print("CLIENT: sent {} bytes".format(n))

    try:
        msg = s.recv(1024)
    except OSError as msg:
        print(msg)
        break
    print("CLIENT: received {} bytes".format(len(msg)))
    print("Received message: {}".format(msg.decode()))

s.close()
