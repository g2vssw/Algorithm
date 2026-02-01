def solution(a, b, n):
    answer = 0
    while True:
        if n < a:
            break
        quotient = n // a
        remainder = n % a
        answer += quotient * b
        n = quotient * b + remainder
    return answer