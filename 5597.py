list_check = [0 for i in range(31)]
for i in range(28):
    num = int(input())
    list_check[num] = 1

for i in range(1, 31):
    if list_check[i] == 0:
        print(i)