def solution(arr, divisor):
    answer = []
    for n in arr:
        if n % divisor == 0:
            answer.append(n)
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
    return answer