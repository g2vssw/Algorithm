def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def cheak(n):
    while True:
        if n == 1:
            return 1
        if n % 2 == 0:
            n = n // 2
            continue
        elif n % 5 == 0:
            n = n // 5
            continue
        return 2

def solution(a, b):
    g = gcd(a, b)
    b = b / g
    answer = cheak(b)
    return answer