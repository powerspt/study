# 26575.py

# d : the number of dogs,
# f : the amount of food per dog in pounds
# p : the price of the food per pound.

N = int(input())

for i in range(N):
    d, f, p = map(float, input().split())
    print("$%.2f" %(d*f*p))

