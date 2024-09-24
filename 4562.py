#4562.py

N = int(input())

for i in range(N):
    x, y = map(int, input().split())
    if x < y:
        print('NO BRAINS')
    else:
        print('MMM BRAINS')