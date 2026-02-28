def solution(t, p):
    answer = 0
    n = len(p)
    for i in range(0, len(t) - n + 1):
        if t[i:i+n] <= p:
            answer += 1
    return answer