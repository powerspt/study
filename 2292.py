'''n = int(input())
num = 1
start=2
end=1
for i in range(1,n):
    start = start +6*(i-1)
    end =  end + 6*i
    if start<=n and n <= end:
        print(i+1)
        break
'''
n = int(input())
cnt = 1
m = 1
while True:
    if n <= m:
        print(cnt)
        break
    m = m + (6 *cnt)
    cnt+=1
    