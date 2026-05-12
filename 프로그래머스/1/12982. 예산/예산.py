def solution(d, budget):
    answer = 0
    d.sort()
    value = 0
    for n in d:
        value += n
        if value <= budget:
            answer += 1
        else:
             break
    return answer