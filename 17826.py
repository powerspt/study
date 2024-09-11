import sys
exam = list(map(int, sys.stdin.readline().split()))
num = int(sys.stdin.readline())
rate = exam.index(num) + 1
if rate <= 5:
    print('A+')
elif rate <= 15:
    print('A0')
elif rate <= 30:
    print('B+')
elif rate <= 35:
    print('B0') 
elif rate <= 45:
    print('C+')   
elif rate <= 48:
    print('C0')
elif rate <= 1505:
    print('F')
