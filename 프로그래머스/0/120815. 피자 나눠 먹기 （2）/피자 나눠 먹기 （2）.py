def solution(n):
    answer = 1
    pizza = 6
    while True:
        if pizza % n == 0:
            break
        pizza += 6
        answer += 1
    return answer