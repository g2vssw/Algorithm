def solution(n):
    answer = ''
    v = n // 2
    if n % 2 == 0:
        answer += "수박" * v
    else:
        answer += "수박" * v + "수"
    return answer