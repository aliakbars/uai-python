#!/usr/bin/env python
import sys

def luasSegitiga(alas, tinggi):
    return alas * tinggi / 2

_, alas, tinggi = sys.argv
print "Segitiga dengan alas {} cm dan tinggi {} cm".format(alas, tinggi)
print "Luas: {} cm2".format(luasSegitiga(float(alas), float(tinggi)))