n = int(input())
#줄 규칙 5 * n / #상부 줄 : 2 * n / #중부 : n / #하부 : n / n
#칸 규칙 n / 3 * n / n
max_line = 5*n
# 줄에 대해
for i in range(max_line):
    if i < 2 * n: # 상부 줄
        print('@'*n, ' '*3*n, '@'*n, sep='')
    elif i < 3 * n: # 중부 한줄
        print('@'*max_line)
    elif i < 4 * n: # 중부 공백 줄
        print('@'*n, ' '*3*n, '@'*n, sep='')
    else: 
        print('@'*max_line)