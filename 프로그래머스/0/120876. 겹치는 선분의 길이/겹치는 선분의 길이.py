def solution(lines):
    answer = 0
    li = []
    black_li = []
    for a, b in lines:
        for i in range(a, b):
            if (i, i + 1) in black_li:
                continue
            if (i, i + 1) in li:
                black_li.append((i, i + 1))
                answer += 1
                continue
            li.append((i, i + 1))
    return answer