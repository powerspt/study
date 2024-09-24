import math
n = int(input())
m = input()
sum = 0

for i in range(n):
    sum += (ord(m[i])-97) * math.pow(31, n)
    
print(sum)
#import math

#print(math.pow(2,3))