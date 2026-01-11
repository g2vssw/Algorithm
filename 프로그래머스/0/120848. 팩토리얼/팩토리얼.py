def fac(num):
    if num == 1:
        return 1
    return num * fac(num - 1)

def solution(n):
    answer = 10
    for i in range(1, 11):
        if fac(i) > n:
            answer = i - 1
            break
    return answer