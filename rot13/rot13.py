# rot13.py - Rot13 en-/de-coder module
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

# encr_char - en-/de-crypt a chararacter
# @char The char to encrypt/decrypt
# @offs Offset into the ascii table
# @rot  Rotation to apply to @char
#
# Returns the en-/de-crypted character
def encr_char(char, offs, rot=13):
    tmp = (char + rot) // (2 * rot + offs)
    char = (char + rot) % (2 * rot + offs)
    if (tmp):
        char += offs
    return char

# encr - rot13 encrypt text
# @pt Plain text
# @mode If set rot47 else rot13
#
# Returns the encrypted text
def encr(pt, mode = 0):
    ct = []

    for i in range(len(pt)):
        char = ord(pt[i])
        if (mode):
            if ((char >= 0x20) and (char <= 0x7d)):
                char = encr_char(char, 0x20, 47)
        else:
            # upper case chars
            if ((char >= 0x41) and (char <= 0x5a)):
                char = encr_char(char, 0x41)
            # lower case chars
            if ((char >= 0x61) and (char <= 0x7a)):
                char = encr_char(char, 0x61)
            # numbers
            if ((char >= 0x30) and (char <= 0x39)):
                char = encr_char(char, 0x30, 5)

        ct.append(chr(char));

    return ct
