import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
f1 = open(file1)
f2 = open(file2)
flag = True
for line1 in f1:
    line2 = f2.readline()
    line1 = line1.split(':')[1].strip()
    line2 = line2.split(':')[1].strip()
    if line1 != line2:
        flag = False
        break
print 'benar' if flag else 'salah'
