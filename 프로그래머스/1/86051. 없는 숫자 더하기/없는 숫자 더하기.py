def solution(numbers):
    answer = 0
    memo = [0] * 10
    for number in numbers:
        memo[number] = 1
    for i in range(10):
        if memo[i] == 0:
            answer += i
    return answer