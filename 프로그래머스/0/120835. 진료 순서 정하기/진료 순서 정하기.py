def solution(emergency):
    answer = []
    sort_emergency = sorted(emergency)[::-1]
    for num in emergency:
        for i in range(len(sort_emergency)):
            if num == sort_emergency[i]:
                answer.append(i + 1)
                break
    return answer