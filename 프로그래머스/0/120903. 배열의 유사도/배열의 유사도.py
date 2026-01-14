def solution(s1, s2):
    answer = 0
    for ss1 in s1:
        for ss2 in s2:
            if ss1 == ss2:
                answer += 1
    return answer