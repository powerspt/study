import sys
num = int(sys.stdin.readline())
for i in range(1, num+1):
    if num == i:
        print(0)
        break
    elif num == i+sum(map(int, str(i))):
        print(i)
        break