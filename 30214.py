import sys

s1 ,s2 = map(int, sys.stdin.readline().split())
#print(type(s1), type(s2))
if s1 >= s2/2:
    print('E')
elif s1 < s2:
    print('H')