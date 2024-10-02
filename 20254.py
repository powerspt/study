# 20254.py

# UR : 지역 예선에서 한 번이라도 풀린 문제?
# TR : 지역 예선에서 한 문제라도 푼 팀
# UO : TOPC에서 한 번이라도 풀린 문제
# TO : TOPC에서 한 문제라도 푼 팀 

# 출력 : 지역 예선 점수  56UR + 24TR + 14UO + 6TO

ur, tr, uo, to = map(int, input().split())
print(56*ur + 24*tr + 14*uo + 6*to)
