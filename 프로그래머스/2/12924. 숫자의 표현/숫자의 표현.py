def solution(n):
    answer = 0
    for num in range(1, n + 1):
        value = 0
        while True:
            
            if value >= n:
                if value == n:
                    answer += 1
                break
            
            value += num
            num += 1
            
    return answer