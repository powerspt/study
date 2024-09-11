import sys 
import math
N = int(sys.stdin.readline())
r = math.fmod(N, 20000303)
sys.stdout.writelines(str(r)) 
# => JudgeFailed
 
'''
# fmod는  x % y가 같은 결과를 반환하지 않을 수 있음
# https://docs.python.org/ko/3/library/math.html
# fmod()는 일반적으로 float로 작업할 때 선호되는 반면 파이썬의 x % y는 정수로 작업할 때 선호
'''