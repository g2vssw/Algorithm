def solution(x):
    answer = True
    num = 0
    for n in str(x):
        num += int(n)
    if x % num != 0:
        answer = False
    return answer