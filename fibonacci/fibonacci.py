#!/usr/bin/env python

# fibonacci.py - Calculate fibonacci series
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

C_DEFLIMIT = "20";

parser = argparse.ArgumentParser(description = "Calculate Fibonacci Series");
parser.add_argument('--limit', '-limit', default=C_DEFLIMIT,
		help="Number of elements to calculate.");
args = parser.parse_args();

try:
	limit = int(args.limit, 0);
except ValueError:
	print("Invalid argument for option \"--limit\": {}. Setting limit = {}"
            .format(args.limit, C_DEFLIMIT));
	limit = int(C_DEFLIMIT, 0);

print("Calculating the first {} elements of the Fibonacci series."
        .format(limit));

fib = [0, 1];
for i in range(2, limit):
	fib.append(fib[i - 1] + fib[i - 2]);

for i in range(limit):
	print("Fib[{}] = {}".format(i, fib[i]));
