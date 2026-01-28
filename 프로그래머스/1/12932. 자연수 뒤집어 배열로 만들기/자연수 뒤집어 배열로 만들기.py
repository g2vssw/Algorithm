def solution(n):
    answer = []
    for s in list(str(n))[::-1]:
        answer.append(int(s))
    return answer