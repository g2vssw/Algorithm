def solution(s):
    answer = True
    p_c = 0
    y_c = 0
    for ss in s:
        if ss in ["p", "P"]:
            p_c += 1
        elif ss in ["y", "Y"]:
            y_c += 1
    if p_c != y_c:
        answer = False
    return answer