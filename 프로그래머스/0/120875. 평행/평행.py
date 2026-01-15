def solution(dots):
    answer = 0
    pairs = [((0, 1), (2, 3)), ((0, 2),(1, 3)), ((0, 3), (1, 2))]
    for a, b in pairs:
        slope1 = (dots[a[0]][0] - dots[a[1]][0]) / (dots[a[0]][1] - dots[a[1]][1])
        slope2 = (dots[b[0]][0] - dots[b[1]][0]) / (dots[b[0]][1] - dots[b[1]][1])
        if slope1 == slope2:
            answer = 1
            break
    return answer