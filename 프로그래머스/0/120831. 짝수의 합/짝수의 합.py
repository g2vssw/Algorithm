def solution(n):
    answer = 0
    for num in range(0, n + 1, 2):
        answer += num
    return answer