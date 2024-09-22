#3733.py

# 입력 인원N, S주식

while True:
    try:
        N, S = map(int, input().split())
        print(S//(N+1))
    except EOFError:
        break