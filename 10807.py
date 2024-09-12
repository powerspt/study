N = int(input())
list_tmp = list(map(int, input().split()))
th = int(input())
cnt=0

for i in list_tmp:
    if i == th:
        cnt+=1
print(cnt)