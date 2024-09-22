# 17256.py

# (a.z + b.x, a.y × b.y, a.x + b.z)

ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())

print(cx - az, cy//ay, cz-ax)
# print(az + bx, ay * by, ax + bz)

#17(az) + 2(bx) = 19(cx)
#16(ay) * 2(by) = 32(cy)
