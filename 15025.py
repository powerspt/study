#15025.py

a, b = map(int, input().split())

count = a + b

if a == 0 and b == 0:
    print('Not a moose')
elif a == b:
   print('Even', a+b)
else:
    if a > b:
        print('Odd', a*2)
    else:
        print('Odd', b*2)