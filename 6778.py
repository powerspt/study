# 입) 첫 라인 안테나 갯수, 둘라인 눈의 갯수
# 출) 에일리언 종료 출력, 매칭X 시 출력 X
import sys 
antena = int(sys.stdin.readline())
eye = int(sys.stdin.readline())

if antena >= 3 and eye <= 4:
    print('TroyMartian')
if antena <= 6 and eye >= 2:
    print('VladSaturnian')
if antena <= 2 and eye <= 3:
    print('GraemeMercurian')