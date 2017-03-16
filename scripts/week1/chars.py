#!/usr/bin/env python

print "Masukkan nama Anda:",
nama = raw_input()

a, e, i = 0, 0, 0
for c in nama:
    if c == 'a':
        a += 1
    elif c == 'e':
        e += 1
    elif c == 'i':
        i += 1

print "Terdapat %d huruf 'a'" % a
print "Terdapat %d huruf 'e'" % e
print "Terdapat %d huruf 'i'" % i