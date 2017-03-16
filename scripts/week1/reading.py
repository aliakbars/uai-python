f = open('angka.in')
line_no = int(f.readline()) # mengetahui jumlah baris
total = 0
for line in range(line_no):
    total += int(f.readline())
print total