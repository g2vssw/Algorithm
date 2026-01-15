def solution(numlist, n):
    answer = []
    li = []
    for num in numlist:
        li.append((abs(num - n), num))
    li.sort()
    p_li = []
    sub = 0
    for s, a in li:
        if s == sub:
            p_li.append(a)
        else:
            answer = answer + p_li[::-1]
            p_li = []
            sub = s
            p_li.append(a)
    answer = answer + p_li[::-1]
    return answer