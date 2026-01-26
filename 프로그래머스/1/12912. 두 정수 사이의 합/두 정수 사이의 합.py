def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    elif a > b:
        answer = (a + b) / 2 * (a - b + 1)
    else:
        answer = (a + b) / 2 * (b - a + 1)
    return answer