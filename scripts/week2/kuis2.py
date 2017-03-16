#!/usr/bin/env python
import sys

filename = sys.argv[1]
f = open(filename)
cases = int(f.readline())

for _ in range(cases):
    c = int(f.readline())
    v1 = sorted([int(x) for x in f.readline().strip().split(' ')])
    v2 = sorted([int(x) for x in f.readline().strip().split(' ')])[::-1]
    total = 0
    for i in range(c):
        total += v1[i] * v2[i]
    print 'Case #{}: {}'.format(_ + 1, total)