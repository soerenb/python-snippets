#!/usr/bin/env python

# rot13.py - Rot13 en-/de-coder
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

import argparse;

# encr - en-/de-crypt a chararacter
# @char The char to encrypt/decrypt
# @offs Offset into the ascii tabe
# @rot  Rotation to apply to @char
# Returns the en-/de-crypted character
def encr(char, offs, rot=13):
	tmp = (char + rot) // (2 * rot + offs);
	char = (char + rot) % (2 * rot + offs);
	if (tmp):
		char += offs;
	return char;

# define and parse command line arguments
parser = argparse.ArgumentParser(description = "Rot13 de-/encoder.");
parser.add_argument('msg', metavar="<MESSAGE>", nargs="?",
        default="Hello World! 4711", help="Message to encrypt.");
parser.add_argument('--input', '-input', help="Input file.");
parser.add_argument('--output', '-output', help="Output file.");
parser.add_argument('--rot47', '-rot47', action="store_const", const=1,
        default=0, help="Encryption mode rot47, default is rot13.");
args = parser.parse_args();

if (args.input == None):
	pt = args.msg;
	print("Plain text:");
	print(pt);
else:
	print("Reading plain text from file \"{}\".".format(args.input));
	fin = open(args.input, "r");
	try:
		pt = fin.read();
	finally:
		fin.close();

ct = [];

for i in range(len(pt)):
	char = ord(pt[i]);
	if (args.rot47):
		if ((char >= 0x20) and (char <= 0x7d)):
			char = encr(char, 0x20, 47);
	else:
		# upper case chars
		if ((char >= 0x41) and (char <= 0x5a)):
			char = encr(char, 0x41);
		# lower case chars
		if ((char >= 0x61) and (char <= 0x7a)):
			char = encr(char, 0x61);
		# numbers
		if ((char >= 0x30) and (char <= 0x39)):
			char = encr(char, 0x30, 5);
	
	ct.append(chr(char));

if (args.output == None):
	print("Encrypted text:");
	print("".join(ct));
else:
	print("Writing cypher text to file \"{}\".".format(args.output));
	fout = open(args.output, "w");
	try:
		fout.write("".join(ct));
	finally:
		fout.close();
