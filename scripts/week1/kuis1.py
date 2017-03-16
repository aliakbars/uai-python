#!/usr/bin/env python

def luas_persegi(s):
    return s ** 2

def luas_persegi_panjang(p, l):
    return p * l

def luas_segitiga(a, t):
    return a * t / 2

def luas_lingkaran(r):
    return 3.14 * (r ** 2)

def luas_trapesium(a, b, t):
    return (a + b) * t / 2

f = open('luas.in')
line_no = int(f.readline()) # mengetahui jumlah baris
luas = []

for line in range(line_no):
    bangun = f.readline().strip() # membuang new line di akhir baris
    if bangun == 'persegi':
        s = float(f.readline())
        luas += [luas_persegi(s)]
    elif bangun == 'persegi_panjang':
        p = float(f.readline())
        l = float(f.readline())
        luas += [luas_persegi_panjang(p, l)]
    elif bangun == 'segitiga':
        a = float(f.readline())
        t = float(f.readline())
        luas += [luas_segitiga(a, t)]
    elif bangun == 'lingkaran':
        r = float(f.readline())
        luas += [luas_lingkaran(r)]
    elif bangun == 'trapesium':
        a = float(f.readline())
        b = float(f.readline())
        t = float(f.readline())
        luas += [luas_trapesium(a, b, t)]

for l in sorted(luas): # dicetak secara berurutan
    print l

print 'Total: {}'.format(sum(luas))