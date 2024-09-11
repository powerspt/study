import sys
import math
# h=세로 크기, v=가로크기, c=cctv 커버리지
h, v, c = map(int, sys.stdin.readline().split())
print(math.ceil(h / c) * math.ceil(v / c))