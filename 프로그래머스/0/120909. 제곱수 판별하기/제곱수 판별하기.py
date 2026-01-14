def solution(n):
    answer = 2
    for i in range(1001):
        if n == i ** 2:
            answer = 1
            break
    return answer