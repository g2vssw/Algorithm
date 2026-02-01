def solution(food):
    answer = '0'
    for i in range(len(food) - 1, 0, -1):
        n = food[i] // 2
        if n >= 1:
            answer = str(i) * n + answer + str(i) * n
    return answer