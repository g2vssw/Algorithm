def solution(arr):
    answer = []
    for n in arr:
        if len(answer) == 0:
            answer.append(n)
        else:
            if n == answer[-1]:
                continue
            else:
                answer.append(n)
    return answer