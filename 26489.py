import sys
cnt = 0
while True:
    try:
        #t = sys.stdin.readline()
        t = input()
        cnt+=1
    except EOFError:
        break
print(cnt)

# input()은 문자열 변환, 줄 바꿈 제거 등 추가적인 과정이 있고, 데이터가 하나 씩 버퍼에 들어가는 반면 sys.stdin.readline()은 문자열로 변환, 줄 바꿈 과정이 없으며 데이터가 한 번에 버퍼에 들어가므로 sys.stdin.readline()이 input() 보다 빠르다.

# Readlines를 사용하면 버퍼의 끝이 어딘지 모르니까 해결 X?