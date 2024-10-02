# 26209.py

a = list(map(int, input().split()))
cnt = 0
for i in a:
    if i != 0 and i != 1:
        cnt += 1

if cnt == 0 :
    print("S")
else:
    print("F")