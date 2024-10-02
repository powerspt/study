# 30999.py

# N개의 문제 후보마다 M명의 출제위원이 찬반 의견(M은 홀수)

cnt = 0

N, M = map(int, input().split())

for i in range(N):
    o = input()
    if o.count('O') > o.count('X'):
        cnt += 1
print(cnt)