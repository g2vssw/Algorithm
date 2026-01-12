def solution(dots):
    w = 0
    h = 0
    for i in range(1, 4):
        if w != 0 and h != 0:
            break
        if dots[0][0] - dots[i][0] != 0:
            w = abs(dots[0][0] - dots[i][0])
        if dots[0][1] - dots[i][1] != 0:
            h = abs(dots[0][1] - dots[i][1])
    answer = w * h
    return answer