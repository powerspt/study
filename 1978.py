# 1978.py

N = int(input())

a = list(map(int, input().split()))
cnt = 0
for i in a:
    if i != 1:
        cnt2 = 0
        for j in range(2, i):
            if i % j == 0:
                cnt2 += 1
        if cnt2 == 0 :
            cnt +=1
print(cnt)