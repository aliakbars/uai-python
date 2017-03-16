#!/usr/bin/env python

print "n:",
n = int(raw_input())
factorial = 1

while n > 0:
    factorial *= n
    n -= 1

print factorial