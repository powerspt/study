import sys

N, X = map(int, sys.stdin.readline().split())

list_tmp = list(map(int, input().split()))

for i in list_tmp:
    if i < X:
        print(i, end=" ")