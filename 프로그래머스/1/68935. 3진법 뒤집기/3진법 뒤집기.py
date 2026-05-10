def solution(n):
    answer = 0
    value = ""
    while True:
        if n <= 2:
            value += str(n)
            break
        value += str(n % 3)
        n = n // 3
    
    for i in range(len(value) - 1, -1, -1):
        answer += (int(value[len(value)-i-1]) * 3 ** i)
    
    return answer