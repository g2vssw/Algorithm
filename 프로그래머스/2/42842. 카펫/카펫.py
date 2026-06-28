def solution(brown, yellow):
    answer = []
    num = brown + yellow
    
    for n in range(num, int(num ** 0.5) - 1, -1):
        if num % n == 0:
            if n >= num // n:
                if yellow == (n - 2) * ((num // n) - 2):
                    answer.append(n)
                    answer.append(num // n)
                    break
    
    return answer