def solution(numbers, k):
    answer = 0
    n = len(numbers)
    cnt = 1
    value = 1
    while True:
        if cnt == k:
            if value == 0:
                answer = n
                break
            answer = value
            break
        value = (value + 2) % n
        cnt += 1
    return answer