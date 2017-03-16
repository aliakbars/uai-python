#!/usr/bin/env python

print "Weight:", # 185
weight = raw_input()
print "Height:", # 81.6
height = raw_input()

bmi = float(weight) / ((float(height)/100) ** 2)
if bmi < 18.5:
    print "underweight"
elif 18.5 <= bmi < 25:
    print "normal"
else:
    print "overweight"