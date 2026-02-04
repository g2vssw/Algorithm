def find_sosu(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    return 1

def solution(n):
    answer = 0
    if n != 2:
        for num in range(2, n + 1):
            if num == 2:
                answer += 1
                continue
            answer += find_sosu(num)
    else:
        answer = 1
    return answer