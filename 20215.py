#20215.py
#w, h corner that is stained with coffee that needs to be to cut off

# 직사각형으로 잘라낼 때와 대각선으로 잘라낼 때의 차이를 출력해보자.

# (w * h) 

# 3 4일 때 직사각형으로 자르면 너비 12 
# 대각선으로 자르면 넓이는 3*4/2 => 6이고 대각선은 루트 (9 + 16) => 5
import math
#print(math.sqrt(25))

# 12 7일 때, 대각선으로 자르면 너비 42, 대각선은 
#print(19-math.sqrt(12**2+7**2))

w, h = map(float, input().split()) 
print("%.9f"%((w+h) - math.sqrt(w**2+h**2)))