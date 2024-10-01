# 15829.py
import math
import sys
a1 = sys.stdin.readline()
a = sys.stdin.readline() 
# sys.stdin.readline()은 왜 안댐?
sum = 0
for i in range(0, len(a)-1):
    print(i, a[i])
    txt = (ord(a[i]) - 96 )
    sum += ((txt * math.pow(31, i)) % 1234567891)
print(int(sum)% 1234567891)
